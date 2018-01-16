
class ParkingSpot:

	def __init__(self, l, f):
		self.location = l
		self.occupied = False
		self.free = f
		print("initialize parking ParkingSpot")

	
	def Area(self):
		raise NotImplementedError("Please Implement the Area method!")
		#Make sure the subclass defines this method
		return None

	def __str__(self):
		price = ""
		if self.free:
			price = "free to park"
		else:
			price = "$10 to park" 
		return "Parking Spot is at location {} and it is {}".format(self.location, price)

#quik test
p = ParkingSpot((1,2,3), True)
print(p)