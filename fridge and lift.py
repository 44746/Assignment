#George West
#16-09-14
#fridge and lift
fridge_width= float(input("please input the fridges width: "))
fridge_length= float(input("please input the fridges length: "))
fridge_depth= float(input("please input the fridges depth: "))

lift_width= float(input("please input the lifts width: "))
lift_length= float(input("please input the lifts length: "))
lift_depth= float(input("please input the lifts depth: "))

fridge_vol = fridge_width*fridge_length*fridge_depth
lift_vol = lift_width*lift_length*lift_depth

if lift_vol >= fridge_vol:
    print("It will fit!")
else:
    print ("It will not fit")
