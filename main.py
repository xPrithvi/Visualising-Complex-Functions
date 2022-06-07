import matplotlib.pyplot as plt
import numpy as np

# Enable Latex
from matplotlib import rc
rc("text", usetex=True)

x_range = np.linspace(start = -2, stop = 2, num = 250)
y_range = np.linspace(start = -2, stop = 2, num = 250)

x_vals, y_vals = np.meshgrid(x_range, y_range)

U = (x_vals**2 - y_vals**2)/(x_vals**4 + y_vals**4 + 2*x_vals**2*y_vals**2)
V = -1*(2*x_vals*y_vals)/(x_vals**4 + y_vals**4 + 2*x_vals**2*y_vals**2)
MAG = np.sqrt(U**2 + V**2)

Fx, Fy = V, U
Hx, Hy = U, -1*V

# Plotting the graph.
fig = plt.figure(figsize = (18, 12))
axes = fig.add_subplot(1, 2, 1)
axes.streamplot(x_vals, y_vals, Hx, Hy, density = 2.5, color = MAG, cmap = "hot", linewidth = 0.5)
axes.axis("scaled")

# Adding title and labels.
axes.set_title("Pòlya Field, $H$", fontsize = 24)
axes.set_xlabel("$Re(z)$", fontsize = 14)
axes.set_ylabel("$Im(z)$", fontsize = 14)

# Drawing the surface.
fig = plt.figure(figsize = (18, 12))
axes = fig.add_subplot(1, 2, 2, projection = "3d")
surface = axes.plot_surface(x_vals, y_vals, MAG, cmap = plt.get_cmap("hot"))

# Adding the title and labels.
plt.title("Plot Title", fontsize = 24)
axes.set_xlabel("$Re(z)$", fontsize = 14)
axes.set_ylabel("$Im(z)$", fontsize = 14)
axes.set_zlabel("$|z|$", fontsize = 14)

# Adding a colour bar.
fig.colorbar(surface, shrink = 0.25, aspect = 5, pad = 0.1)
plt.tight_layout()
