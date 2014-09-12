#George West
#12-09-2014
#Height and Weight converter

height_inches = float(input("Please input your height in inches; "))
height_centi = height_inches*2.54

weight_stone = float(input("Please input your weight in stone; "))
weight_kilo = weight_stone*6.364


print("Your height in centimetres is {0} and your weight in kilograms is {1}".format(height_centi, weight_kilo))
