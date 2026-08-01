from sympy import sympify, lambdify, symbols
import numpy as np
import matplotlib.pyplot as plt

# Ask the user for information
equation_text = input("Enter an equation: ")
x_min = float(input("Enter x minimum: "))
x_max = float(input("Enter x maximum: "))

# Turn the text into a math function
x = symbols("x")
expression = sympify(equation_text)
f = lambdify(x, expression, "numpy")

# Generate 200 x-values
xs = np.linspace(x_min, x_max, 200)

# Calculate y-values
ys = f(xs)

# Replace invalid values (inf, -inf, NaN) with NaN
ys = np.array(ys, dtype=float)
ys[~np.isfinite(ys)] = np.nan

# Create a small gap around x = 0 to prevent connecting
# across discontinuities like 1/x
gap = (x_max - x_min) / 200

for i in range(len(xs)):
    if abs(xs[i]) < gap:
        ys[i] = np.nan

# Save valid points to CSV
with open("points.csv", "w") as file:
    file.write("x,y\n")
    for i in range(len(xs)):
        if np.isfinite(ys[i]):
            file.write(f"{xs[i]},{ys[i]}\n")

print("Saved points to points.csv")

# Plot the graph
plt.figure(figsize=(6, 6))
plt.plot(xs, ys)
plt.scatter(xs, ys, s=10)
plt.title(f"y = {equation_text}")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()