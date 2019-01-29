#!/usr/bin/env python3
#
# CSCI 5448 - OOAD - Homework 1, Question 4 solution
# name: Timothy Mason;   Collaborators: none

# Class definition for Shapes base class
class Shapes:
	def __init__(self, CenterX, CenterY, Radius):
		self.x = CenterX
		self.y = CenterY
		self.r = Radius

# Class definition for Circle subclass
class Circle(Shapes):
	def printMe(self):
		print("Circle at {},{} with radius {}" % (self.x, self.y, self.r))

# Class definition for Square subclass
class Square(Shapes):
	def printMe(self):
		print("Square at {},{} with radius {}" % (self.x, self.y, self.r))

# Class definition for Triangle subclass
class Triangle(Shapes):
	def printMe(self):
		print("Triangle at {},{} with radius {}" % (self.x, self.y, self.r))

if __name__ == "__main__":
	print("University of Colorado at Boulder")
	print("CSCI 5448 - Object Oriented Analysis And Design")
	print("")
	print("Solution to Homework 1, Question 4")
	print("name: Timothy Mason")
	print("collaborators: none")

	# load the "database"

	# sort the data

	# "draw" the shapes