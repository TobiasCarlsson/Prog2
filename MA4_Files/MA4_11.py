#!/usr/bin/env python3.9

#from person import Person
import random
import matplotlib.pyplot as plt
import math

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

def main():

    Monte_carlo(10000)



if __name__ == '__main__':
	main()
