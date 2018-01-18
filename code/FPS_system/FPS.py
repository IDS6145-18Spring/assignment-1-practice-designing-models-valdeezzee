import math, time, random
import numpy as np
from Location import Location
from Handicap import Handicap
from Regular import Regular
from Compact import Compact
from MultiLevel import MultiLevel
from SingleLevel import SingleLevel
from Sensor import Sensor


def CreateParkingLots(parkingLots):
	#create a random amount of parking spots for sim
	handicap = []
	comapct = []
	regular = []	

	'''Create some parking spots for the parking lots'''
	for i in range(0,10):
		handicap.append(Handicap("A-" + str(i), 0.0, Sensor(), True))
		comapct.append(Compact("B-" + str(i), 12.0, Sensor()))
		regular.append(Regular("C-" + str(i), 20.0, Sensor()))

	'''Create some parking lots and initialize them'''
	sL = SingleLevel(Location(1,2,3),handicap,3,4,5)
	mL = MultiLevel(Location(1,2,3),comapct,3,4,5,6)

	'''Print out the parking lots you just created'''
	'''Print out all the available parking spots'''	
	print(sL)
	for spot in sL.GetParkingSpots():
		print(spot)

	print()

	print(mL)
	for spot in mL.GetParkingSpots():
		print(spot)	

def CreateRandomLocations():
	x = random.randrange(0,10)
	y = random.randrange(0,10)
	z = random.randrange(0,10)
	randLocation = (x,y,z)
	return randLocation



def Simulate():
	'''This is where you will get the user input and search for a spot'''
	print()



def main():
	
	#create parking lots
	parkingLots = []
	CreateParkingLots(parkingLots)

	Simulate()

if __name__ == '__main__':
	main()
