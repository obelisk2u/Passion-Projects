from vpython import *

# Set up the scene
scene = canvas(title="3D Solar System Simulation", width=800, height=600, background=color.black)
scene.caption = "\nRotate: Drag with left mouse button\nZoom: Scroll mouse wheel\nPan: Right-click or drag with both mouse buttons.\n"

# Create the Sun
sun = sphere(pos=vector(0, 0, 0), radius=2, color=color.yellow, emissive=True)
sun_label = label(pos=sun.pos, text="Sun", xoffset=0, yoffset=50, space=30, height=10, color=color.white, box=False)

# Hover text for the Sun
def on_mouse_move(evt):
    picked_obj = scene.mouse.pick  # Detects the object the mouse is over
    if picked_obj == sun:
        scene.title = "The Sun: A massive ball of burning gas at the center of the solar system."
    else:
        scene.title = "3D Solar System Simulation"

scene.bind("mousemove", on_mouse_move)

# Function to create a planet
class Planet:
    def __init__(self, name, radius, texture, distance, orbital_speed):
        self.body = sphere(pos=vector(distance, 0, 0), radius=radius, texture=texture)
        self.orbit_distance = distance
        self.angle = 0
        self.orbital_speed = orbital_speed
        self.label = label(pos=self.body.pos, text=name, xoffset=0, yoffset=50, space=30, height=10, color=vector(1, 1, 1), box=False)  # Use vector for white color

    def update_position(self):
        self.angle += self.orbital_speed
        self.body.pos = vector(self.orbit_distance * cos(self.angle), 0, self.orbit_distance * sin(self.angle))
        self.label.pos = self.body.pos

# Create Earth with texture
earth_texture = textures.earth  # Use built-in Earth texture
earth = Planet("Earth", 0.6, earth_texture, 8, 0.02)
planets = [earth]

# Animation loop
while True:
    rate(30)  # Lower the frame rate to 30 frames per second to reduce CPU load
    for planet in planets:
        planet.update_position()
