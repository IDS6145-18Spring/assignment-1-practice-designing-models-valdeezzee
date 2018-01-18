import math, time, random
import numpy as np
from Location import Location
from Handicap import Handicap
from Regular import Regular
from Compact import Compact
from MulitLevel import MulitLevel
from SingleLevel import SingleLevel
from Sensor import Sensor


def CreateParkingLots(parkingLots):
	#create a random amount of parking spots for sim
	print("creating spots")
	locations = []

		

	#for i in range(0,5):
	#	tempLoc = CreateRandomLocations()
	#	locations.append(tempLoc)
	#	parkingSpots.append(Handicap(tempLoc, False, 12.0, True, False))
	#for l in locations:
	#	print(l)
	#for p in parkingSpots:
	#	print(p)

	h = Handicap("A-1", 0.0, "Sensor", True)
	c = Compact("A-2", 12.0, "Sensor")
	r = Regular("A-3", 20.0, "Sensor")

	sL = SingleLevel(Location(1,2,3),h,3,4,5)
	mL = MulitLevel(Location(1,2,3),c,3,4,5,6)

	print(sL)
	print(mL)
	print(h)
	print(h.Area())
	print(c)
	print(c.Area())
	print(r)
	print(r.Area())
	


	# create new random locations
	

def CreateRandomLocations():
	x = random.randrange(0,10)
	y = random.randrange(0,10)
	z = random.randrange(0,10)
	randLocation = (x,y,z)
	return randLocation



def Simulate():
	print("here")



def main():
	
	#create parking spots
	parkingLots = []
	CreateParkingLots(parkingLots)

	Simulate()
	l = Location(1,2,3)
	#print(l)

if __name__ == '__main__':
	main()
