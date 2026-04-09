# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "matplotlib>=3.10.8",
#     "numpy>=2.4.4",
# ]
# ///

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(1,10,100)

A = np.piecewise(t, [t<2, (t>=2) & (t<=8), t>8], [0, lambda t: (t-2)/(8-2), 1])
B = np.piecewise(t, [t<2, (t>=2) & (t<=8), t>8], [1, lambda t: (8-t)/(8-2), 0])
M = np.piecewise(t, [t<2, (t>=2) & (t<=5), (t>5) & (t<=8), t>8], [0, lambda t: (t-2)/(5-2), lambda t: (8-t)/(8-5), 0])

plt.figure(figsize=(8,5))
plt.plot(t, A, "r", label="A")
plt.plot(t, B, "b", label="B")
plt.plot(t, M, "g", label="M")

plt.xlabel("t")
plt.title("Conjuntos difusos")
plt.legend()
plt.grid()

plt.show()