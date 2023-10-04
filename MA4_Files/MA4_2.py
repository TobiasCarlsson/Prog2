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


	
def main():
	x = 30
	t1 = pc()
	print(fib_numba(x))
	t2 = pc()
	print(fib_py(x))
	t3 = pc()
	print(f'Numba: {round(t2-t1,4)}')
	print(f'Python: {round(t3-t2,4)}')

	#f = Person(5)
	#print(f.get())
	#f.set(7)
	#print(f.get())

if __name__ == '__main__':
	main()
