"""Another practice problem for OOP"""
import numpy #so I can do average


class Dataset(object):
	"""I don't know what this will contain"""
	def __init__(self,nums):
		"""Initializes a dataset"""
		self.data = nums

	def __str__(self):
		"""Prints the contents nicely"""
		return str(self.data)

	def add_value(self,value):
		"""Adds a value, called value, to the data set

		>>> D1 = Dataset([1,2,3])
		>>> D1.add_value(4)
		>>> print D1
		[1, 2, 3, 4]
		"""

		self.data.append(value)


	def compute_mean(self):
		"""Returns the mean of numbers in dataset"""
		return numpy.mean(self.data)

if __name__ == '__main__':
    import doctest
    doctest.testmod()