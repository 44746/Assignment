#George West
#19-09-14
#money counter

value=int(input("Please input your amount of money; "))
twenty = value//20
remainder = value%20
ten = remainder//10
remainder = remainder%10
five = remainder//5
remainder = remainder%5
two = remainder//2
remainder = remainder%2
one = remainder//1
remainder = remainder%1
print("""You entered {0}, you will need:
{1} twenty pound note(s)
{2} ten pound note(s)
{3} five pound note(s)
{4} two pound coin(s)
{5} one pound coin(s)""".format(value,twenty,ten,five,two,one))
      
        
