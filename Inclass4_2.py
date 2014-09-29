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