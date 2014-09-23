#George West
#23-09-14
#spot check - weights q2

weight=int(input("Please enter the weight: "))
remainder = weight
hundred= remainder//100
remainder = remainder%100
fifty=remainder//50
remainder=remainder%50
ten=remainder//10
remainder=remainder%10
five=remainder//5
remainder=remainder%5
two=remainder//2
remainder=remainder%2
one=remainder


print("""You entered {0} to balance this value you will need:
{1} hundred gram weight(s)
{2} fifty gram weight(s)
{3} ten gram weight(s)
{4} five gram weight(s)
{5} two gram weight(s)
{6} one gram weight(s)""".format(weight,hundred,fifty,ten,five,two,one))
