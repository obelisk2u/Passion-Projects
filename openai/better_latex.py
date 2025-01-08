from pytex import Pytex

latex_code = r"""
\documentclass{article}
\usepackage{amsmath}
\begin{document}
1. \( 5 = 7x - 16 \)
   \( 7x = 21 \)
   \( x = 3 \)

2. \( 2 = 3 - 5 - x \)
   \( x = 3 - 5 - 2 \)
   \( x = -4 \)
\end{document}
"""

formatted_latex = Pytex(latex_code).format()
print(formatted_latex)