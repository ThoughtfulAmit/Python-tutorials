# Press F5 to run this file
# 1: printing basic O/P on screen

print "1: printing basic O/P on screen"
print "Hello, World!"

# 2: Numbers and Math

print "\n2: Numbers and Math"
print 2+2
print 4-3
print 18/7
print 18/7.0
print 18.0/7
print 18/7.
print 9%4
print 8%4
print 8.75%.5
print 6*6
print 6**2
print -5**4 # It's equivalent of -(5^4) = -(625)
print (-5)**4


# 3: Variables

print "\n3: Variables"
x = 18
print x
y= 54
print x+y

g = input("Enter number here: ")
print g+1

# 4: Modules and Functions

print "\n4: Modules and Functions"
print pow(5,4)
print abs(-18)

import math                     #importing "math" module to use function "floor"
print math.floor(18.7)          #use Ctrl+Space to get other functions
print math.sqrt(81)

a_sqrt = math.sqrt              #assigning the function to our own variable
print a_sqrt(36)

# 5: Saving the programs

x = raw_input ("Enter name: ")
print "Hey " + x
raw_input ("Press <enter> ")    #to hold screen in cmd

