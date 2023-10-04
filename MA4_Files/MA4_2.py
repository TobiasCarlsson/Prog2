#!/usr/bin/env python3.9

#C++

#MonteCarlo
import random
import math
import matplotlib.pyplot as plt
from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future
import time

#Numba
from numba import njit

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))
	
def main():
	x = input("What is the fib num")
	start_time = time.time()
	fib_numba(x)
	t_numba = start_time - time.time()
	start_time = time.time()
	fib_py(x)
	t_py = start_time - time.time()
	print(t_numba)
	print(t_py)

	#f = Person(5)
	#print(f.get())
	#f.set(7)
	#print(f.get())

if __name__ == '__main__':
	main()
