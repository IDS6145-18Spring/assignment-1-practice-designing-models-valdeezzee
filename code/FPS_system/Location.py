''' This class defines a location in the world
	where a parking spot can exist'''
import numpy as np
class Location:

	def __init__(self, x, y, z):
		''' Initialize a 3d vector tht represents the parking spot locations'''
		self.xCoord = x
		self.yCoord = y
		self.zCoord = z
		self.vectorLocation = np.array([x,y,z])

	def Distance(self, userLocation):
		''' I'm using 3d vectors to represent locations'''
		dist = np.linalg.norm(self.vectorLocation - userLocation)
		#return the distance between the user and the current parking spot
		return dist

	def CurrentLocation(self):
		'''Get the current location of this object'''
		return self.vectorLocation

	def __str__(self):
		return "Parking spot is located at: {} ".format(self.vectorLocation)
