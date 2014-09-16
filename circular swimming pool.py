#George West
#16-09-14
#circular swimming pool
import math
radius = float(input("Please input the radius of your pool in meters: "))
depth = float(input("Please input the depth of your pool in meters: "))
volume = radius**2 * math.pi
litres = volume*1000
print("You will need {0:.2f} litres to fill your pool".format(litres))
