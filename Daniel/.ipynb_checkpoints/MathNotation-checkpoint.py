# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # MATH NOTATION

import matplotlib.pyplot as plt
# plain text
plt.title('alpha > beta')

print(plt.title(r'$\alpha > \beta$'))

from sympy import symbols
x, y, z = symbols('x y z')
expr = 2*x + y
expr2 = expr.subs(y, 2*x**2 + z**(-3))
expr2

# +

from sympy import symbols, exp
n0, Qv, R, T = symbols('n0 Qv R T')
expr = n0*exp(-Qv/(R*T))
expr
# -


