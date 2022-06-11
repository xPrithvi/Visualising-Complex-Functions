import matplotlib.pyplot as plt
import numpy as np

"""# Enable Latex
from matplotlib import rc
rc("text", usetex=True)"""

x_range = np.linspace(start = -2, stop = 2, num = 250)
y_range = np.linspace(start = -2, stop = 2, num = 250)
x_vals, y_vals = np.meshgrid(x_range, y_range)
z = x_vals + 1j*y_vals

FUNC = np.sin(z)/z**2
Hx, Hy = np.real(FUNC), -1*np.imag(FUNC)
MAG = np.absolute(FUNC)

# Plotting the graph.
plt.figure(figsize = (9, 6))
plt.streamplot(x_vals, y_vals, Hx, Hy, density = 2.5, color = MAG, cmap = "hot", linewidth = 0.5)
plt.axis("scaled")

# Adding title and labels.
plt.title("Pòlya Field, $H$", fontsize = 24)
plt.xlabel("$Re(z)$", fontsize = 14)
plt.ylabel("$Im(z)$", fontsize = 14)

plt.show()
