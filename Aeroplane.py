#George West
#23-09-14
#Aeroplane

import math




degree = float(input("Please input the degree the plane has travelled from north: "))
distance= float(input("Please input the distance the plane has travelled: "))
east_degree = 90-degree
east_radian = east_degree*0.0174532925
north_radian = degree*0.0174532925
north = math.cos(north_radian)*distance
east = math.cos(east_radian)*distance
print("The plane has travelled {0}km north and {1}km east".format(north,east))
