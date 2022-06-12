import matplotlib.pyplot as plt
import numpy as np

"""# Enable Latex
from matplotlib import rc
rc("text", usetex=True)"""

class ComplexFunc():

    def __init__(self, expression):
        self.func_string = expression

    def PolyaField(self, dimensions, density):
        NUM = round((dimensions[1]-dimensions[0])*(dimensions[3]-dimensions[2])*density)
        print(NUM)
        x_range = np.linspace(start = dimensions[0], stop = dimensions[1], num = NUM)
        y_range = np.linspace(start = dimensions[2], stop = dimensions[3], num = NUM)
        x_vals, y_vals = np.meshgrid(x_range, y_range)
        z = x_vals + 1j*y_vals

        func = eval(self.func_string)
        Hx, Hy = np.real(func), -1*np.imag(func)

        # Plotting the graph.
        plt.figure(figsize = (9, 6))
        plt.quiver(x_vals, y_vals, Hx, Hy)
        plt.axis("scaled")

        # Adding title and labels.
        plt.title("Pòlya Field, $H$", fontsize = 24)
        plt.xlabel("$Re(z)$", fontsize = 14)
        plt.ylabel("$Im(z)$", fontsize = 14)

        plt.show()

FUNC = ComplexFunc("1/np.cos(z)")
FUNC.PolyaField(dimensions = [-3, 3, -3, 3], density = 2)
