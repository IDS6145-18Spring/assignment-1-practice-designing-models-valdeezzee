from ParkingSpot import ParkingSpot
class Compact(ParkingSpot):

	def __init__(self, number, cost, sensor):
		print("Compact")
		ParkingSpot.__init__(self, number, cost, sensor)

	def Area(self):
		l = 20
		w = 7
		return l * w