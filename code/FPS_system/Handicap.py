from ParkingSpot import ParkingSpot
class Handicap(ParkingSpot):

	def __init__(self):
		self.vanAccesible = false

	def Area(self):
		print("setting area of spot")