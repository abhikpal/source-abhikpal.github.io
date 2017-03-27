import numpy as np
import math

def foo(some_number):
	return some_number*math.sqrt(some_number)

if __name__ = '__main__':
	k = int(raw_input("Enter a number: "))
	print "After doing the magic, the number is: {}".format(foo(k))

