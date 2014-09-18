#George West
#18-09-14
#Denary to binary
denary=int(input("Please input a denary number: "))
binary_string = ""
while denary > 0:
     binary_string = str(denary %2) + binary_string
     denary = denary // 2

print("The binary equivalent is {0}".format(binary_string))
