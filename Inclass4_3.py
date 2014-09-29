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



