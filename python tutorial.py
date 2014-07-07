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

g = input("Enter number here: ")    #treats user's I/P as an expression not string
print g+1

# 4: Modules and Functions

print "\n4: Modules and Functions"
print pow(5,4)
print abs(-18)

import math                     #importing "math" module to use function "floor"
print math.floor(18.7)          #use Ctrl+Space or Tab for auto-completion
print math.sqrt(81)

a_sqrt = math.sqrt              #assigning the function to our own variable
print a_sqrt(36)

# 5: Saving the programs

x = raw_input ("Enter name: ")  #treats user's I/P as a string
print "Hey " + x
raw_input ("Press <enter> ")    #to hold screen in cmd

# 6: Strings

print "\n6: Strings"
print 'hey user, '
print "I\'m stupid! "           #look for the escape character '\'
print "user said,\"YES!!\" to that statement"
a = "amit"
b = " sharma"
print a + b

# 7: More on Strings

print "\n7: More on Strings"
num = 21
print num + 5

num = str(21)
print "amit is " + num + " years old"
num2 = 21                               #can't use num as integer anymore bcz it's a string now

print "he will be " + `num2 + 1` + " yrs old this yr"   #using backtics(above Left Tab key)
num3 = 21

print "he was " + repr(num3 - 1) + " yrs old last yr"

# 8: Diff bw input and raw_input
# Already explained above with examples

# 9: Sequences and Lists

print "\n9: Sequences and Lists"
family = ['mom','dad','bro','sis']
print family
print family[3]             #counting forward starts from 0
print family[-1]            #counting backward starts from -1
print 'amit'[2]

# 10: Slicing

print "\n10: Slicing"
example = [10,20,30,40,50,60]
print example[3:5]          #first argument(arg) is included not second
print example[3:6]
print example[-3:-1]        #example[-3:0] unlike [3:6] (extending upper limit by 1 to get last element) won't give the last element
print example[-6:]
print example[0:]
print example[:]
print example[:3]
print example[1:5:2]
print example[-6:-1:2]
print example[::2]

# 11: Editing Sequences

print "\n11: Editing Sequences"
print [3,4,6] + [3,2,1]
print 'amit ' + 'sharma'

print 'amit' * 10
print [3] * 10

print example[2] * 10
print [example[2]] * 10

name = 'amit'
print 'm' in name
print 'mom' in family

# 12: More List Functions

print "\n12: More List Functions"
print len(family)
print len(example)
print max(example)
print min(example)
print list('amit')
example[2] = 35
print example
del example[2]

# 13: Slicing List

print "\n13: Slicing List"
example = list('amitabh')
print example
example[4:]=list('hey')
print example
example[4:]=list('sharma')
print example
example = [7,8,9]
example[1:1]=[3,5,6]    #adding elements bw arg1 n arg2, where arg2 not included
print example
example[1:5]=[]         #deleting elements
print example

# 14: Intro to Methods

print "\n14: Intro to Methods"
example = [21,15,30]
print example
example.append(45)
print example
example2 = ['I', 'am', 'stupid','stupid','stupid','amigo']
print example2.count('stupid')
one = [1,2,3]
two = [4,5,6]
one.extend(two)
print one

# 15: More methods

print "\n15: More methods"
one = list('amit')
print one.index('i')

one.insert(2,'S')
print one
print one.pop(3)    #returns the value
print one
one.remove('S')
print one
one.reverse()
print one

# 16: Sort and Tuples

print "\n16: Sort and Tuples"
new = [23,12,45,54,23]
new.sort()
print new

print sorted('AmitSharma')

amit = (23,12,45,54,23)     #tuple can't be modified unlike list
print amit
print amit[2]


# 17: Strings n Stuff

print "\n17: Strings n Stuff"
amit = "Hey there %s, howz u doing %s"
var1 = ('user', 'hero')
print amit % var1
var2 = ('tuna', 'fish')
print amit % var2
example = "Howz u doing"
print example.find('doing')

# 18: Cool String Methods

print "\n18: Cool String Methods"
example = ['I', 'am', 'stupid', 'amigo']
glue = '9'
print glue.join(example)

str1 = "I am StuPId AmIGo"
print str1.lower()
print str1.upper()
print str1

truth = "I am 20 years, NO, 21 years old"
print truth.replace('years', 'yrs')         #replaces both 'years'

# 19: Dictionary

print "\n19: Dictionary"
book = {'FirstName': 'Amit', 'LastName': 'Sharma'}      #pair of keys and values
print book
print book['FirstName']
ages = {'Dad':'42', 'Mom':'41'}
print ages
print ages['Dad']

book.clear()
print book
tuna = ages.copy()
print tuna

print tuna.has_key('Mom')
print tuna.has_key('Sis')

# 20: If Statement

print "\n20: If Statement"
tuna="fish"
if tuna == "fish" :
    print '\nThis is a fish!'

# 21: else and elseif

print "\n21: else and elseif"
fish = "tuna"
if fish == "bass" :
    print "this is bass!"
elif fish == "slamon":
    print "This is slamon!"
elif fish == "tuna":
    print "this is tuna!"
else:
    print "I don't know what this is!"

# 22: Nesting statements

print "\n22: Nesting statements"
thing = "animal"
animal = "cat"
if thing == "animal":
    if animal == "cat":
        print "This is a cat!"
    else:
        print "I don't know this animal"
else:
    print "I don't know what this is!"


# 23: Comparison Operators

print "\n23: Comparison Operators"
print 9<7
print 9<=9
print 9!=3

one = [21,22,23]
two = [21,22,23]
print one == two
print one is two            #only true if same object
three = four =[4,5,6]
print three is four

pizza = "pizzahut"
print 's' in pizza
print 'p' in pizza

# 24: And and OR

print "\n24: And and OR"
print "dog" < "cat"         #alphabetical order

example = 6
if example > 3 and example < 10:
    print 'number is bw 3 and 10'       #BOTH conditions must be true

if example > 3 or example < 4:
    print 'this works'                  #AT-LEAST ONE condition must be true

# 25: For and While Loops

print "\n25: For and While Loops"
b = 1
while b <= 10:
    print b
    b += 1

gl = ['bread', 'milk', 'egg']
print gl

for food in gl:                         #food is the variable which will hold diff value at each iteration
    print 'I want ' + food

# 26: Infinite Loops and Break

print "\n26: Infinite Loops and Break"
ages = {'Dad':'45', 'Mom':'44', 'Lisa':'24'}        #Dictionary
print ages                          #Notice the alphabetic order in O/P

for item in ages:
    print item

for item in ages:
    print item, ages[item]

while 1:
    name = raw_input("Enter name(to exit type 'quit'): ")
    if name == 'quit':
        break

# 27: Building Functions

print "\n27: Building Functions"
def whatsup(x):
    return 'whats up ' + x

print whatsup('amit')

def plusten(y):
    return y+10

print plusten(44)

# 28: Default Parameters

print "\n28: Default Parameters"
def name(first='amit',last='sharma'):
    print 'First Name: %s Last Name: %s' % (first,last)

name()
name('stupid', 'amigo')
name('stupid')
name(last='amigo')

# 29: Multiple Parameters

print "\n29: Multiple Parameters"
def list(*food):                # '*' used to define a tuple for unknown multiple args
    print food
list('apples')
list('one','two','three')

def profile(name,*ages):
    print name
    print ages

profile('amit', 21,20,25,19)

# 30: Parameter Types

print "\n30: Parameter Types"
def cart(**items):              # '**' used to define a dictionary
    print items

cart(apples=4,peaches=6,mangoes=10)

def profile2(first,last,*ages,**items):
    print first, last
    print ages
    print items

profile2('amit','sharma',32,30,31,24, bacon=4, saus=64)     #Notice the numeric order in O/P for Dictionary elements

# 31: Tuples as Parameters

print "\n31: Tuples as Parameters"
def example1(a,b,c):
    return a+b*c
tuna = (5,7,3)
print example1(*tuna)

def example3(**this):
    print this
bacon={'mom':45, 'dad':46}
print example3(**bacon)

