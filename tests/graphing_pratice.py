# The Training Grounds
from functools import cache
import numpy as np
import math
from matplotlib import pyplot as plt


@cache
def summation_math(start, end, f):
    if start > end:
        return 0
    return f(end) + summation_math(start, end - 1, f)


# Example usage
if __name__ == "__main__":
    print("Testing out numpy, scipy, and matplotlib")
    f = lambda x: (2*x + 4*x)
    x_coordinates = [x for x in range(0, 12)]
    y_coordinates = [f(x) for x in range(0,12)]
    plt.plot(x_coordinates, y_coordinates)
    plt.show()
