#Inclass4 Part 2

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I

print "I will now count my chickens:" #it prints the string in the quotes

print "Hens", 25 + 30 / 6 	# the division happens first then addition
print "Roosters", 100 - 25 * 3 % 4 	#multiply first, then use mod, then subtract

print "Now I will count the eggs:"	#prints this string here

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6 	#Division and mod first, then at and subtract

print "Is it true that 3 + 2 < 5 - 7?"	#prints this string right here

print 3 + 2 < 5 - 7 	#prints false because the statement is incorrect math

print "What is 3 + 2?", 3 + 2 	#prints the string and the math function
print "What is 5 - 7?", 5 - 7	#prints the string and another math function

print "Oh, that's why it's False."	#prints the string

print "How about some more."	#prints the string

print "Is it greater?", 5 > -2       #prints the string and true
print "Is it greater or equal?", 5 >= -2  #prints the string and true
print "Is it less or equal?", 5 <= -2   #prints the string and false

#PART II

days = "Mon Tue Wed Thu Fri Sat Sun"        #assigns the string into the variable days
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"    #assigns the string into the variable months
  
print "Here are the days: ", days      #prints the string and the variable
print "Here are the months: ", months   #prints the string and the variable

#PART III

the_count = [1, 2, 3, 4, 5]	        #stores the array into the variable the count
fruits = ['apples', 'oranges', 'pears', 'apricots']   #stores an array of strings into the variable 
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']   #stores an array of strings and integers in the variable

# for loop here, prints this is count and every number in the count variable
for number in the_count:
    print "This is count %d" % number       

# for loop here, prints a fruit of type, and every string in the variable fruit
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# Prints i got and every member in change
# Use %r format when you don't know
#if the elements are strings or integers
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# prints evrey element 0 to 5 that was added to elements
for i in elements:
    print "Element was: %d" % i





    #Inclass4 Part 3

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I

#Use the code from Lecture14.py to create and change the 
#'stuff' list; Then comment on each line of the code below
#what it does, and what the result is

ten_things = "Apples Oranges Crows Telephone Light Sugar"

#print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "The 'stuff' list: ", stuff

#Working with Dictionaries
d1 = {'a': 'some value', 'b': [1, 2, 3, 4]} #can contain lists

#Access an element by key
print d1['a']

#Add an element (a pair key: value) to the dict
d1[7] = 'an integer'
print d1

#Check if the dict contains a certain key
print "b" in d1

#Delete a value

del d1[7] # deletes the value at location 7 from the dict d1
print d1 # prints out the dictionary d1

#Use functions defined for dictionaries
print "Keys", d1.keys()
print "Values", d1.values()

print stuff[1]
print stuff[-1] 
print stuff.pop()
print ' '.join(stuff) 
print '#'.join(stuff[3:5]) 

#PART II

#Create comments where marked with # to explain the code below

# Creates a dictionary name states , key is the state name and 
# the value is the abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# creates a dictionary named cities and key is the abbreviation of state
# and value is the city 
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# addis two keys and values to the dities dictionary
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# prints 10 of _ characters
# prints the values in citites for the NY and OR keys
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# prints 10 _ characters
# prints the values in the states for Michigan and Florida
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# prints 10 _ characters
# prints prints the values in cities dictionary for the values in states
# dictionary for the Michigan and Florida
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# prints 10 _ characters
# for loop for the states dictionary and prints each key and value
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# prints 10 _ characters
# For loop through the dicites dictionary, prints each key and value
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# prints 10 _ characters
# for loop through the states dictionary, prints each key and value
# prints the value in cities dictionary for each abbreviation for states
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])