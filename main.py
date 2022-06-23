import matplotlib.pyplot as plt
import numpy as np

# Enable Latex
from matplotlib import rc
rc("text", usetex=True)

class PolyaField():

    def __init__(self, complex_function = "z**2", dimensions = [-1, 1, -1, 1], density = 5):
        NUM = round((dimensions[1]-dimensions[0])*(dimensions[3]-dimensions[2])*density)
        self.x_range = np.linspace(start = dimensions[0], stop = dimensions[1], num = NUM)
        self.y_range = np.linspace(start = dimensions[2], stop = dimensions[3], num = NUM)
        self.x_vals, self.y_vals = np.meshgrid(self.x_range, self.y_range)
        z = self.x_vals + 1j*self.y_vals

        self.func_string = complex_function
        self.func = eval(complex_function)
        self.Hx, self.Hy = np.real(self.func), -1*np.imag(self.func)

    def VF(self, zoomed = False):

        # Plotting the graph.
        figure, axes = plt.subplots()
        axes.quiver(self.x_vals, self.y_vals, self.Hx, self.Hy)

        # Adding title and labels.
        axes.set_title("Pòlya Field, $H$", fontsize = 24)
        axes.set_xlabel("$Re(z)$", fontsize = 14)
        axes.set_ylabel("$Im(z)$", fontsize = 14)

        # Zoomed plot.
        if zoomed is False:
            pass
        else:
            axes_zoomed = axes.inset_axes([0.65, 0.65, 0.3, 0.3])
            NUM = round((zoomed[1]-zoomed[0])*(zoomed[3]-zoomed[2])*zoomed[4])
            x_range = np.linspace(start = zoomed[0], stop = zoomed[1], num = NUM)
            y_range = np.linspace(start = zoomed[2], stop = zoomed[3], num = NUM)
            x_vals, y_vals = np.meshgrid(x_range, y_range)
            z = x_vals + 1j*y_vals

            func = eval(self.func_string)
            Hx, Hy = np.real(func), -1*np.imag(func)
            axes_zoomed.quiver(x_vals, y_vals, Hx, Hy)

        plt.show()

    def SP(self):
        # Plotting the graph.
        plt.figure(figsize = (16, 16))
        plt.streamplot(self.x_vals, self.y_vals, self.Hx, self.Hy)
        plt.axis("scaled")

        # Adding title and labels.
        plt.title("Pòlya Field, $H$", fontsize = 24)
        plt.xlabel("$Re(z)$", fontsize = 14)
        plt.ylabel("$Im(z)$", fontsize = 14)

        plt.show()

    def curl(self):
        pass

PF = PolyaField("1/z**2", density = 5)
PF.VF(zoomed = [-0.1, 0.1, -0.1, 0.1, 1000])
