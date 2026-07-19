from sympy import sympify, lambdify, symbols
import numpy as np
import matplotlib.pyplot as plt

# the equation, written as text
equation_text = "sin(x)"

# turn the text into real math
x = symbols("x")
expression = sympify(equation_text)
f = lambdify(x, expression, "numpy")

# calculate y for 50 x values from -5 to 5
xs = np.linspace(-5, 5, 50)
ys = f(xs)

# show the points
for i in range(len(xs)):
    print(f"x = {xs[i]:.1f}   y = {ys[i]:.1f}")

# plot the curve
plt.plot(xs, ys)
plt.scatter(xs, ys)
plt.title(equation_text)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()