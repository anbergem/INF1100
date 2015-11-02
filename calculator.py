from scitools.std import StringFunction, linspace, zeros
from matplotlib.pyplot import plot, show

class Calculator:
	''' '''
	def __init__(self, a, b):
		self.a, self.b = a, b

	#def __add__(self, other):
	#	return self.a + self.b + other.a + other.b

	def add(self):
		'''Calculates the sum of a and b'''
		return self.a + self.b

	def subtract(self):
		'''Calculates the difference between a and b'''
		a = self.a
		b = self.b
		return a - b

	def multiply(self):
		'''Calculates the product of a and b'''
		a = self.a; b = self.b
		return a * b

	def divide(self):
		'''Calculates the division between a and b, given as a float'''
		a, b = self.a, self.b
		return a/float(b)

	def change_variables(self, a, b):
		'''Changes the variables used in the calculator'''
		self.a, self.b = a, b

	def function(self, f, x):
		'''Calculates a given function f, at a point or an array x'''
		f = StringFunction(f)
		return f(x)


if __name__ == '__main__':

	c = Calculator(10, 5)
	#d = Calculator(10, 5)
	#print c + d
	print 'Adding: ', c.add()
	print 'Subtracting: ', c.subtract()
	print 'Multiplying: ', c.multiply()
	print 'Divifing: ', c.divide()
	print 'Changeing variables...'
	c.change_variables(6, 3)
	print 'Now adding: ', c.add()
	print 'Now trying functions...'
	print 'f(x) = x^2, x = 2: ', c.function('x**2', 2)
	print 'Trying with array...'
	c.change_variables(linspace(-5, -3, 3), linspace(-1, 1, 3))
	print 'Adding linspace(-5, -3, 5), linspace(-1, 1, 5):'
	print c.add()
	print 'f(x) = x^2, x = linspace(-1, 1, 11): '
	print  c.function('x**2', linspace(-1, 1, 21))
	x = linspace(-5, 5)
	plot(x, c.function('x**2+x**4-3', x))
	raw_input()

'''
Bergem$ python Calculator.py
Adding:  15
Subtracting:  5
Multiplying:  50
Divifing:  2.0
Changeing variables...
Now adding:  9
Now trying functions...
f(x) = x^2, x = 2:  4
Trying with array...
Adding linspace(-5, -3, 5), linspace(-1, 1, 5):
[-6. -4. -2.]
f(x) = x^2, x = linspace(-1, 1, 11):
[ 1.    0.81  0.64  0.49  0.36  0.25  0.16  0.09  0.04  0.01  0.    0.01
  0.04  0.09  0.16  0.25  0.36  0.49  0.64  0.81  1.  ]
'''






