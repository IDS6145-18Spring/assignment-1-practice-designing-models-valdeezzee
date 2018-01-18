## Smart City (My Problem) Model
Staring coding framwork for the Fast Parking Search

(remove:  Starting coding framework for the (insert your exact problem here.)
(remove: learn to describe your code a bit, link the files and provide a brief explanation what each file is doing for your model and simulation)

[**FPS.py**](../code/FPS_system/FPS.py) - This will be where you start your simulation. It will create parking lots and assign parking spots to it. It will the print out the parking lots and spots you have just created

[**ParkingLot.py**](../code/FPS_system/ParkingLot.py) - This is the base parking lot class. It contains a Location and Parking Spots

[**SingleLevel.py**](../code/FPS_system/SingleLevel.py) - this is type of parking lot. 

[**MultiLevel.py**](../code/FPS_system/MultiLevel.py) - this is a type of parking lot. It will contain different floors

[**ParkingSpot.py**](../code/FPS_system/ParkingSpot.py) - This is the base parking spot class. It contains a sensor, cost, and a spot number

[**Regular.py**](../code/FPS_system/Regular.py) - this is a type of parking spot

[**Compact.py**](../code/FPS_system/Compact.py) - this is a type of parking spot

[**Handicap.py**](../code/FPS_system/Handicap.py) - this is a type of parking spot

[**Location.py**](../code/FPS_system/Location.py) - this class is used for containing a location for the parking lot you are searching for. It can also be used to give the user a location to later compare distance

[**Sensor.py**](../code/FPS_system/Sensor.py) - this class defines a sensor that detects vehicles that are parked over it, life span, and a timer for detecting how long it take for the user to get to the spot