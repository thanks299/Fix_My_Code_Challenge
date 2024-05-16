#!/usr/bin/python3
"""
This module defines a class Square.
"""

class Square:
	"""
	A class used to represent a Square
	"""

	width = 0
	height = 0

	def __init__(self, *args, **kwargs):
		"""
		Initialize the square with optional width and height

		Parameters:
		*args (tuple): Additional positional arguments (not used)
		**kwargs (dict): Key-value pairs for width and height
		"""
		for key, value in kwargs.items():
			setattr(self, key, value)

	def area_of_my_square(self):
		"""
		Calculate the area of the square

		Returns:
		int: The area of the square
		"""
		return self.width * self.height

	def permiter_of_my_square(self):
		"""
		Calculate the perimeter of the square

		Returns:
		int: The perimeter of the square
		"""
		return 2 * (self.width + self.height)

	def __str__(self):
		"""
		Provide a string representation of the square

		Returns:
		str: The width and height of the square separated by a '/'
		"""
		return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
	"""
	Main entry point of the module
	"""
	s = Square(width=12, height=9)
	print(s)
	print(s.area_of_my_square())
	print(s.permiter_of_my_square())
