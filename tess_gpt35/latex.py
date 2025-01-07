import subprocess
import os

def generate_and_compile_latex(latex_code, output_dir="output.tex", pdf_viewer=""):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    latex = start + latex_code + end
    print(latex)
    tex_file = os.path.join(output_dir, "output.tex")
    pdf_file = os.path.join(output_dir, "output.pdf")
    
    with open(tex_file, "w") as f:
        f.write(latex)
    
    try:
        subprocess.run(
            ["pdflatex", "-output-directory", output_dir, tex_file],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error during LaTeX compilation: {e}")
        return

    if pdf_viewer: 
        subprocess.run([pdf_viewer, pdf_file])
    else:  
        if os.name == "nt": 
            os.startfile(pdf_file)
        elif os.name == "posix": 
            subprocess.run(["open" if sys.platform == "darwin" else "xdg-open", pdf_file])

# Example LaTeX code
start = r'''
\documentclass{article}
\usepackage{amsmath}
\begin{document}
'''

end = r'''\end{document}'''
