#!/usr/bin/env python3
#
# CSCI 5448 - OOAD - Homework 1, Question 4 solution
# name: Timothy Mason;   Collaborators: none
import random
import math

# Class definition for Shapes base class
class Shapes:
	def __init__(self, CenterX=0.0, CenterY=0.0, Radius=1.0):
		self.x = float(CenterX)
		self.y = float(CenterY)
		self.r = float(Radius)
		self.distFromCtr = math.sqrt( self.x**2.0 + self.y**2.0 )	# Euclidian distance from the origin

	def __updateDist(self):
		self.distFromCtr = math.sqrt( self.getX()**2.0 + self.getY()**2.0 )

	def setX(self, CenterX = 0.0):
		self.x = float(CenterX)
		self.__updateDist()

	def setY(self, CenterY = 0.0):
		self.y = float(CenterY)
		self.__updateDist()

	def setCenter(self, Center = (0.0, 0.0)):
		self.x = float(Center[0])
		self.y = float(Center[1])
		self.__updateDist()

	def setRadius(self, Radius = 0.0):
		self.r = float(Radius)

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getCenter(self):
		return (self.x, self.y)

	def getRadius(self):
		return self.r

	def getDistFromCtr(self):
		return self.distFromCtr

	# The __repr__ method allows the object to return a string representation of itself.  This is used automatically
	# by the Python print() built-in function.
	def __repr__(self):
		return "Generic shape at ({},  {)} with radius {}".format(self.getX(), self.getY(), self.getRadius())

	# Implement comparison operators to allow use of the Python built-in sort function.  Comparisons will be based
	# on the distance of the shape center from the origin
	def __eq__(self, other):
		return (self.getDistFromCtr() == other.getDistFromCtr())

	def __ne__(self, other):
		return (self.getDistFromCtr() != other.getDistFromCtr())

	def __lt__(self, other):
		return (self.getDistFromCtr() < other.getDistFromCtr())

	def __le__(self, other):
		return (self.getDistFromCtr() <= other.getDistFromCtr())

	def __gt__(self, other):
		return (self.getDistFromCtr() > other.getDistFromCtr())

	def __ge__(self, other):
		return (self.getDistFromCtr() >= other.getDistFromCtr())


# Class definition for Circle subclass
class Circle(Shapes):
	def __repr__(self):
		return "Circle at ({:.2f}, {:.2f}) with radius {:.2f}".format(self.getX(), self.getY(), self.getRadius())

# Class definition for Square subclass
class Square(Shapes):
	def __repr__(self):
		return "Square at ({:.2f}, {:.2f}) with radius {:.2f}".format(self.getX(), self.getY(), self.getRadius())

# Class definition for Triangle subclass
class Triangle(Shapes):
	def __repr__(self):
		return "Triangle at ({:.2f}, {:.2f}) with radius {:.2f}".format(self.getX(), self.getY(), self.getRadius())

# "main program" ...
if __name__ == "__main__":
	print("University of Colorado at Boulder")
	print("CSCI 5448 - Object Oriented Analysis And Design")
	print("")
	print("Solution to Homework 1, Question 4")
	print("")
	print("name: Timothy Mason")
	print("collaborators: none")
	print("")
	print("")

	# load the "database" by building a list of 20 randomly selected shapes at random locations and sizes
	catalog = [Circle, Square, Triangle]
	database = []
	for i in range(0,20):
		database.append(catalog[random.randint(0,len(catalog)-1)](
			random.uniform(-100.0,100.0),		# Randomly generated x coordinate of center to constructor
			random.uniform(-100.0,100.0),		# Randomly generated y coordinate of center to constructor
			random.uniform(0.0,10.0))			# Randomly generated radius of the shape to the constructor
		)
	# sort and "draw" the data
	for s in sorted(database):
		print(s)