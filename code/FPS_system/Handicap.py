from ParkingSpot import ParkingSpot
class Handicap(ParkingSpot):

	def __init__(self):
		self.vanAccesible = false

	def Area(self):
		l = 20
		''' I added 5 to represent the space between adjoining parking spots '''
		if vanAccesible:
			w = 11 + 5
		else:
			w = 8 + 5
		return l * w