#prime Number checker 1
x=0
number=int(input("to check for prime, type a number between 2 and 200: "))
if number in range (2,201):
    primefile = open("prime200.txt","r")
    mystring="not a prime number"

    for i in primefile:
        if number == int(i.strip()):
            x = 1
            print str(number) + " is a prime number"
        else:
            pass
    if x == 0:
        print mystring
    else:
        pass
else:
    print "not a valid number, just sayin" 
        
