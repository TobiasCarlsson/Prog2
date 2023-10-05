#Student: Tobias Karlsson
#Mail: tobias.karlsson.2002@student.uu.se
#Reviewed by: Naser Shabani
#Reviewed date: 20231005


import random
import math
import numpy as np
import concurrent.futures as future
from time import perf_counter as pc


def hypersphere(n,d): # Without PPE
	#Filter, list comprehension
	def lessThanOne(num):
		if num <= 1:
			return True
		else:
			return False
	
	samples_radii = [sum([random.uniform(-1,1)**2 for _ in range(d)]) for i in range(n)]
	
	c = len(list(filter(lessThanOne,samples_radii)))

	print('dimensions: ',d,', samples: ', n,', nc: ', c,', approx: ', 2.0**d*c/n)
	return 2.0**d * c/n

def hypersphere_exact(d):
	#Lambdafunktion
	f = lambda x : math.pi**(x/2) / (math.gamma(x/2+1))
	print('dimensions: ', d,', hypersphere_exact: ', f(d))
	return f(d)

def hypersphere_PP(n, d, proc): #with PPE
	
	with future.ProcessPoolExecutor() as ex:
		processes = []
		result = []
		npp = n//proc
		for _ in range(10):
			p = ex.submit(hypersphere, npp, d)
			processes.append(p)
		for p in processes:
			result.append(p.result())

	print('dimensions: ',d,', samples: ', n,', processes: ', proc,', approx: ', sum(result)/proc )
	return sum(result)/proc

def main():
	t1 = pc()
	hypersphere(10000000, 11)
	hypersphere_exact(2)
	t2 = pc()
	hypersphere_PP(10000000, 11, 10)
	hypersphere_exact(2)
	t3 = pc()

	print('time No PPE', t2-t1)
	print('time PPE', t3-t2)
	
if __name__ == '__main__':
	main()