import random
import math
import numpy as np

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
    
    return estimated_volume, actual_volume

if __name__ == "__main__":
    n = int(input("Enter the number of random points (n): "))
    d = int(input("Enter the number of dimensions (d): "))
    
    estimated_volume, actual_volume = monte_carlo_hypersphere(n, d)
    
    print(f"Estimated Volume: {estimated_volume}")
    print(f"Actual Volume (using formula): {actual_volume}")