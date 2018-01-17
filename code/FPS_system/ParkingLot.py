
class ParkingLot():
	"""docstring for ParkingLot"""
	def __init__(self, arg):
		super(ParkingLot, self).__init__()
		self.arg = arg
		
	def __str__(self):
		return "This is a {} ParkingLot".format(str(self.__class__.__name__))