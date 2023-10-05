#!/usr/bin/env python3.9

from person import Person

import random
import math
import matplotlib.pyplot as plt
from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future
import numpy as np


#Numba
from numba import njit

def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))
    
@njit
def fib_numba(n):
    if n<= 1:
        return n
    else:
        return fib_numba(n-1) + fib_numba(n-2)

def graph(q,w):
    
    x = range(q,w)
    y_cpp = []
    y_numba = []
    y_py = []

    for i in x:
        
        t1 = pc()
        f = Person(i)
        f.fib()
        t2 = pc()
        fib_numba(i)
        t3 = pc()
        fib_py(i)
        t4 = pc()

        y_cpp.append(t2-t1)
        y_numba.append(t3-t2)
        y_py.append(t4-t3)

    plt.plot(x ,y_cpp, "r", label="C++")
    plt.plot(x, y_numba, "g", label="Numba")
    plt.plot(x, y_py, "b", label="py")

    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title('r = C++, g = Numba, b = Py')
    plt.savefig(str(q) + "to" + str(w) + 'Fib_TimeComparison.png')

def time47():
    x = 47

    t1 = pc()
    f = Person(x)
    print(f'C++: {f.fib()}')
    t2 = pc()
    print(f'numba: {fib_numba(x)}')
    t3 = pc()


    print(f'C++: {round(t2-t1,4)}')
    print(f'Numba: {round(t3-t2,4)}')

def is_inside_hypersphere(point, d):
    # Check if the point is inside the d-dimensional hypersphere
    squared_sum = sum(x**2 for x in point)
    return squared_sum <= 1

def monte_carlo_hypersphere(n, d):
    points = np.random.rand(n, d)  # Generate n random points in d dimensions
    
    # Use filter and lambda to count points inside the hypersphere
    inside_points = list(filter(lambda point: is_inside_hypersphere(point, d), points))
    
    # Calculate the volume of the hypersphere
    estimated_volume = len(inside_points) / n * (2**d)
    actual_volume = math.pi**(d/2) / math.gamma(d/2 + 1)

    print(f"Estimated Volume: {estimated_volume}")
    print(f"Actual Volume (using formula): {actual_volume}")

    return estimated_volume, actual_volume


def Monte_carlo(n):    
    # Lists to store x and y coordinates of points
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []
    inside_circle = 0
    
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        # Check if the point is inside the unit circle
        if x**2 + y**2 <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)
    
    # Approximate π using the Monte Carlo method
    estimated_pi = 4 * inside_circle / n
    
    print("1. Number of points inside the circle (nc):", inside_circle)
    print("2. Approximation of π ≈", estimated_pi)
    print("3. Python's math.pi:", math.pi)
    
    # Create a scatter plot of the points
    plt.figure(figsize=(6, 6))
    plt.scatter(x_inside, y_inside, color='red', marker='.')
    plt.scatter(x_outside, y_outside, color='blue', marker='.')
    plt.title("Estimating π using Monte Carlo Simulation")
    plt.xlabel("x")
    plt.ylabel("y")
    
    # Save the plot as a PNG file
    plt.savefig(str(n) + "monte_carlo_pi.png")
    
    # Display the plot
    plt.show()


def main():
    n = 100
    d = 100
    num_points = 10000

    Monte_carlo(num_points)

    graph(20,30)
    time47()
    graph(30,45)

    estimated_volume, actual_volume = monte_carlo_hypersphere(n, d)
    

if __name__ == '__main__':
    main()
