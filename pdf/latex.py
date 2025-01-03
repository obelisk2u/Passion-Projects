import subprocess
import os

def generate_and_compile_latex(latex_code, output_dir="output", pdf_viewer=""):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # File paths
    tex_file = os.path.join(output_dir, "output.tex")
    pdf_file = os.path.join(output_dir, "output.pdf")
    
    # Save LaTeX code to .tex file
    with open(tex_file, "w") as f:
        f.write(latex_code)
    
    # Compile LaTeX file to PDF using pdflatex
    try:
        subprocess.run(
            ["pdflatex", "-output-directory", output_dir, tex_file],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error during LaTeX compilation: {e}")
        return

    # Open the PDF file using the system's default viewer
    if pdf_viewer:  # If a specific viewer is provided
        subprocess.run([pdf_viewer, pdf_file])
    else:  # Use the default viewer
        if os.name == "nt":  # Windows
            os.startfile(pdf_file)
        elif os.name == "posix":  # macOS/Linux
            subprocess.run(["open" if sys.platform == "darwin" else "xdg-open", pdf_file])

# Example LaTeX code
latex_code = r'''
\documentclass{article}
\usepackage{amsmath}
\begin{document}
Hello, World! Here is some math: \( E = mc^2 \).
\[
\int_0^\infty e^{-x^2} \, dx = \frac{\sqrt{\pi}}{2}
\]
\end{document}
'''

generate_and_compile_latex(latex_code)
