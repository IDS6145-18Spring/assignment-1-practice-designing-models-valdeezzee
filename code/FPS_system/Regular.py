from ParkingSpot import ParkingSpot
class Regular(ParkingSpot):

	def __init__(self, number, cost, sensor):
		print("Regular")
		ParkingSpot.__init__(self, number, cost, sensor)

	def Area(self):
		l = 20
		w = 8
		return l * w
