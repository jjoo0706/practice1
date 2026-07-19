from sympy import sympify, lambdify, symbols
import numpy as np

# the equation, written as text
equation_text = "x**2"

# turn the text into real math
x = symbols("x")
expression = sympify(equation_text)
f = lambdify(x, expression, "numpy")

# calculate y for 11 x values from -5 to 5
xs = np.linspace(-5, 5, 11)
ys = f(xs)

# show the points
for i in range(len(xs)):
    print(f"x = {xs[i]:.1f}   y = {ys[i]:.1f}")