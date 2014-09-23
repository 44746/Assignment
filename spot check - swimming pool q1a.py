#George West
#23-09-14
#spot check - swimming pool q1a

import math
width=float(input("Please input the width of your pool: "))
length=float(input("Please input the length of your pool: "))
depth=float(input("Please input the depth of your pool: "))
main_section_volume = length*width*depth
circle_radius=width/2
circle_area= math.pi*circle_radius**2
half_circle_volume = (circle_area/2)*depth
pool_volume = main_section_volume + half_circle_volume
print("The volume of your pool is {0}".format(pool_volume))
      
