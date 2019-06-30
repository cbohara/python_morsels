import math


class Circle:
	def __init__(self, radius=1):
		self._radius = radius

	def __repr__(self):
		return f'Circle({self.radius})'

	@property
	def radius(self):
		return self._radius

	@radius.setter
	def radius(self, radius):
		if radius < 0:
			raise ValueError("Radius cannot be negative")
		self._radius = radius

	@property
	def diameter(self):
		return self._radius * 2

	@diameter.setter
	def diameter(self, diameter):
		self._radius = diameter / 2

	@property
	def area(self):
		return math.pi * self._radius ** 2
