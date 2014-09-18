#George West
#18-09-14
#binary to denary

binary=input("Please input a binary number: ") 
total = 0
if binary[0] == '1':
    total =total+128
if binary[1] == '1':
    total =total+64
if binary[2] == '1':
    total =total+32
if binary[3] == '1':
    total =total+16
if binary[4] == '1':
    total =total+8
if binary[5] == '1':
    total =total+4
if binary[6] == '1':
    total =total+2
if binary[7] == '1':
    total =total+1

print("Your denary number is {0}".format(total))
