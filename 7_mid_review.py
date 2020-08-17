### Hamida Khatri

### July 27, 2020

####### PYTHON BASICS #######

x = "elephant"
#1: print what type of item this is (image, str, int, etc)

print(type(x))


x = 5
#2: print what type of item this is (image, str, int, etc)

print(type(x))


x = "The name of this course is Python for Data Analytics."
#3: print the 2nd-7th letters

print(x[1:7])


a = "Elephants are beautiful."
#4: print how many letters are in the above sentence

print(len(a))


a = "   There are a lot of extra spaces!   "
#5: get rid of the white space

# strip() function will remove leading and trailing whitespaces ONLY!

print(a.strip())

# To remove multiple white spaces

def rid_space(string):
  return string.replace(" ", "")
print(rid_space(a))

a = "My NAme is FRaNk and I LIke to Eat FOod!"
#6: print this in all lower-case

print(a.lower())

#7: print this in all upper-case

print(a.upper())

tart = "The rain in Spain stays mainly in the plain"
#8: How do I know if "stays mainly" is in the above text?

import re

staymain = re.findall("stays mainly", tart)
if staymain:
  print("Yes, it is!")
else:
  print("Nopes!")


#9: How do I know if "mainstay" is in the above text?

import re

staymain = re.findall("mainstay", tart)
if staymain:
  print("Yes, it is!")
else:
  print("Nopes!")


a = "BLUE"
b = "GATORADE"
#10: Print both of these words, side by side

print(a + " " + b)

#11: Print both of these words, on 2 separate lines

print(a)
print(b)

#12: Create a simple addition program.
    #Tell the user to pick two numbers
    #Add the two numbers together
      #Make sure you:
        #Define it in a function (you pick the name)
        #Make sure the text can be read as a number (float)
        #Include delays
        #Calculate and print the answer
        #Include a restart option, asking the user if they'd like to continue adding, or exit

import time

print("Let's play a game!")

time.sleep(1)
print()

      #Make sure you:
        #Define it in a function (you pick the name)
        #Make sure the text can be read as a number (float)
        #Include delays
        #Calculate and print the answer
        #Include a restart option, asking the user if they'd like to continue adding, or exit


def math_game():
  user_input1 = float(input("Enter 1st number: "))

  time.sleep(.1)
  print()

  user_input2 = float(input("Enter 2nd number: "))
  
  print()

  total = user_input1 + user_input2
  print("The total is: ",total)

  print()
        
  continuation = input("Would you like to continue? ")

  if continuation == "yes" or continuation == "yeah" or continuation == "yep" or continuation == "y":
    print()
    math_game()

  if continuation == "no" or continuation == "nope" or continuation == "na" or continuation == "n":
    print()
  print("Thank you for playing with us!")

math_game()


#Working with lists -----

#13: Print all items in the list, one by one:
laptops = ["HP", "SONY", "APPLE", "DELL"]

for elem in laptops:
  print (elem)


#14: Add an item, "mask" to the following list:
necessities = ["phone", "laptop", "keys", "chapstick"]

necessities.append("mask")

#15: print the above list (should incude "mask")

print(necessities)

#16: print the first item in the above list

print(necessities[0])

#17: print the 2nd & 3rd item in the above list

print(necessities[1:3])

#18: now, remove "mask" and re-print the above list

necessities.remove("mask")
print(necessities)

#------------
#Working with loops:

#19: Print i as long as i is less than 6

i = 0
while i < 6:
  print(i)
  i += 1

  #how do you prevent the loop from running forever?

i = 0 
while i < 6:
  print(i)
  if i == 4:
    break
  i += 1


## ANEESA'S Solution
  ## Print i as long as i is less than 6
  ## How do you prevent the loop from running forever?

i = 1
while i < 6:
  print(i)
  i += 1 # this will break the while loop , if I remove it, it will keep running
          # i is the interator

  
#Working with math:

#20: round 11.4 UP to the nearest whole #
  #hint: import something

import math
x = math.floor(11.4)
print(x)

## OR 
print(round(11.4))


#21: Write a Python command to generate random float numbers in a specific numerical range.
  #remember what you need to import

import random

print(random.randrange(1,3000))

## Need to mention the size as well and the range in between you want to have the random numbers

import random
import numpy

print(numpy.random.uniform(0.0, 300.0, size=(10)))


#-----------

#22: Create and print a dictionary 
  #must include:
    # - at least 3 words and their associated definitions

my_dict = {
  "color" : "The property possessed by an object of producing different sensations on the eye as a result of the way the object reflects or emits light.",
  "emotion" : "A natural instinctive state of mind deriving from one's circumstances, mood, or relationships with others.",
  "armor" : "The metal coverings formerly worn by soldiers or warriors to protect the body in battle."
}

print(my_dict)


#23: Print all key names in the dictionary, one by one

for key in my_dict.keys():
  print(key)

 
#24: Print all values in the dictionary, one by one

for value in my_dict.values():
  print(value)

#25: Print how many items (key-value pairs) the above dictionary has

print(len(my_dict))

## Mike's Solution

for key, value in my_dict.items():
  print(key, ": ", value)

## ANEESA'S Code

student_score = {'Ritika': 5, 'Sam': 7, 'John': 10, 'Aadi': 8}

[print(key, value) for key, value in student_score.items()]

#26: Add an item (key-value pair) to the above dictionary

new_item = ({"stationary" : "Not moving or not intended to be moved."})

#27: Re-print your updated dictionary

new_item.update(my_dict)
print(new_item)

#28: Remove the last item you added to this list

del new_item["stationary"]
print(new_item)

#--------
#Working with if/else/elif
#29: Ask the user a yes or no question (your choice!)

howdy = input("Are you a mathematician? ")
print(howdy)

  #30: if yes, print a statement
    #if
if howdy == "yes":
  print("WOW! I am your fan!")

  #31: if no, print a statement
    #elif
elif howdy == "no":
  print("Oh, that's alright.")

  #32: if anything else, print a statement
    #else
else:
  print("That sucks!")

#More math!
  #33: Create a data set of 16 numbers

import math

data_set = (1,3,4,6,8,10,12,14,15,17,18,19,20,22,25,28)

  #34: Print the lowest# in the set
data_set = min(1,3,4,6,8,10,12,14,15,17,18,19,20,22,25,28)
print(data_set)

  #35: Print the highest# in the set
data_set = max(1,3,4,6,8,10,12,14,15,17,18,19,20,22,25,28)
print(data_set)


## OR ##

import numpy
x = numpy.random.uniform(1.0, 100.0, 16)
print(x)
print(min(x))
print(max(x))


#36 - print me the square root of 144

import math

x = math.sqrt(144)
print(x)


#-------
#-------
#-------
###END OF PARTNER COLLAB 07/27/20

"""Aneesa's Quiz"""

# Here are two lists of box office performances for Marvel and DC movies.
marvel_box_office = [783, 370, 708, 519, 757, 1214, 585, 677, 714, 2732, 1153, 263, 1346, 2046, 890, 449, 623, 880, 622, 1405, 863, 1518, 850, 773, 821, 644, 1127]

dc_box_office = [374, 391, 1000, 185, 11, 219, 1085, 668, 873, 746, 310, 821, 657, 52, 1147, 364, 1061]

# How many movies are in the Marvel box office?
n_marvel = len(marvel_box_office)

# How many movies are in the DC box office?
n_dc = len(dc_box_office)

# What is the total gross of Marvel movies?
total_gross_marvel = sum(marvel_box_office)

# What is the total gross of DC movies?
total_gross_dc = sum(dc_box_office)

# What is the HIGHEST gross for a Marvel movie.
max_gross_marvel = max(marvel_box_office)

# What is the HIGHEST gross for a DC movie.
max_gross_dc = max(dc_box_office)

# Calculate the average gross of Marvel movies.
avg_marvel_gross = sum(marvel_box_office) // len(marvel_box_office)

# Calculate the average gross of DC movies.
avg_dc_gross = total_gross_dc / n_dc




"""For the next few activities you will use the list of DC Universe members in the `dc_members` list below.

In the cell below add "Joker" to the end of the `dc_members` list.
"""

dc_members = ["Superman", "Batman", "Wonder Woman", "Aquaman", "The Flash", "Harley Quinn"]

# Write an expression in the line below to add "Joker" to the `dc_members` list.
dc_members.append("Joker")


"""Items in lists are accessed according to an item's index.  In the next exercise write the code to assign the 4th item in the list to the variable `idx_member`.

**HINT: Remember zero-indexing!**
"""

dc_members == ["Superman", "Batman", "Wonder Woman", "Aquaman", "The Flash", "Harley Quinn", "Joker"]

# Write an expression to assign `idx_member` to the 4th item of the list.
idx_member = dc_members[3] # index 3



"""What is the last item in `dc_members`?  Remember there was a special way of accessing items at the end of a list...

Write an expression to assign the variable `last_item` to the last value in the list.
"""

dc_members == ["Superman", "Batman", "Wonder Woman", "Aquaman", "The Flash", "Harley Quinn", "Joker"]

# Write the code to assign `last_item` to the last item in the list.
last_item = dc_members[-1]


##########################


dc_members == ["Superman", "Batman", "Wonder Woman", "Aquaman", "The Flash",]

# Find the index for "Wonder Woman" in `dc_members`
#set var to indx
#what is an index?

indx = dc_members.index("Wonder Woman")


##########################

fav_animals = ["elephant", "dolphin", "tiger"]
# Write an expression to add "shark" to the list

#append

fav_animals.append("shark")


##########################

#Write an expression to assign "caterpillar" to the 2nd item in the list

fav_animals.insert(1, "caterpillar")

fav_animals[1] = "caterpillar"

##########################

fav_animals = ["elephant", "dolphin", "tiger", "bee", "bird"]

#print Dolphin through bee
#range_animal

print(fav_animals[1:4])

range_animal = fav_animals[1:4] # 1 is index, 4 is actual numeric position

##########################

fav_animals = ["elephant", "dolphin", "tiger", "bee", "bird"]
fav_animals.pop(0) #removes 1st item: elephant
del fav_animals[0] #removes 1st item: dolphin

#print output
  #tiger
  #bee
  #bird

##########################

#Create a dictionary called aneesa_dict:
  #favorite color = green
  #favorite car = honda
  #favorite food = pizza
  #favorite book = cats cradle

aneesa_dict = {
    "favorite color": "green",
    "favorite car": "honda",
    "favorite food": "pizza",
    "favorite book": "cats cradle"
}

#########################

dc_members == ["Superman", "Batman", "Wonder Woman", "Aquaman", "The Flash", "Harley Quinn", "Joker"]

# Complete the expression below to select "Batman", "Wonder Woman" and "Aquaman" from the list below.
rng_members = dc_members[1:4]
print(rng_members)

#########################

"""There are multiple ways to remove an item from a list.

In the cell below choose one way to remove "Joker" from the list.
"""

dc_members = ["Superman", "Batman", "Wonder Woman", "Aquaman", "The Flash", "Harley Quinn", "Joker"]

# Write an expression that will remove "Joker" from the dc_members list.
dc_members.pop(-1)
print(dc_members)

#########################

"""Try using another method to remove "Batman" from the list."""

dc_members = ["Superman", "Batman", "Wonder Woman", "Aquaman", "The Flash", "Harley Quinn"]

# Write an expression to remove "Batman" from the list that is different from the one you used above.
del dc_members[1]
print(dc_members)

#########################

"""## Dictionaries

Let's practice with dictionaries.

First, in the cell below define a dictionary with at least 2 keys.  The keys and values can be anything.
"""

# Create a dictionary and assign it to the my_first_dictionary variable.
my_first_dictionary = {
    "key": 123
}

#########################

"""The next couple of questions will use the `marvel_movies` dictionary below."""

marvel_movies = {
    "Avengers: Endgame": 2732,
    "Avengers: Infinity War": 2046,
    "Marvel's The Avengers": 1518,
    "Avengers: Age of Ultron": 1405,
    "Black Panther": 1346,
    "Iron Man 3": 1214,
    "Captain America: Civil War": 1153,
    "Captain Marvel": 1127,
    "Spider-Man 3": 890,
    "Spider-Man Homecoming": 880,
    "Guardians of the Galaxy 2": 863,
    "Thor: Ragnorak": 850,
    "Spider-Man": 821,
    "Spider-Man 2": 783,
    "Guardians of the Galaxy": 773,
    "The Amazing Spider-Man": 757,
    "Captain America: The Winter Soldier": 714,
    "The Amazing Spider-Man 2": 708,
    "Doctor Strange": 677,
    "Thor: The Dark World": 644,
    "Iron Man 2": 623,
    "Ant-Man and the Wasp": 622,
    "Iron Man": 585,
    "Ant-Man": 519,
    "Thor": 449,
    "Captain America: The First Avender": 370,
    "The Incredible Hulk": 263
}

"""`marvel_movies` has the name of a Marvel movie as its key and the value is the gross earnings from the movie.

With the information, write an expression to retrieve the earnings for "Thor" and assign it to the `thor_earnings` variable.
"""

# Get the earnings of "Thor" using the marvel_movies dictionary.
thor_earnings = marvel_movies.get("Thor")

##########################

"""How can you determine how many items are in a dictionary?

In the cell below populate `n_marvel_dict` with the number of items in the `marvel_movies` dictionary.
"""

# Complete the expression below to assign n_marvel_dict to the number of items in marvel_movies
n_marvel_dict = len(marvel_movies)

#########################

"""Add a new entry to `marvel_movies` for the upcoming Black Widow movie and assign its value to 0."""

# Complete the expression below to add "Black Widow" to the dictionary and set its value to 0.
marvel_movies["Black Widow"] = 0

#########################

"""We discussed multiple ways to remove an item from a dictionary.

In the cell below choose one way to remove a value from a dictionary and remove "Black Widow" from `marvel_movies`.
"""

# In the line below write code to remove "Black Widow" from the `marvel_movies` dictionary.
marvel_movies.pop("Black Widow")

#########################

"""Are you sure Black Widow was removed?

Write an expression to test whether the key "Black Widow" is in `marvel_movies`.  Assign the output to the `in_marvel_movies` variable.
"""

# Write an expression to test if "Black Widow" is in marvel_movies.
in_marvel_movies = "Black Widow" in marvel_movies

#########################

"""Based on the [list methods documentation](https://docs.python.org/3/tutorial/datastructures.html) can you determine how many times the number 5 occurs in the list below?

Code should output the answer to populate the `n_five` variable.
"""

list_of_ints = [6, 5, 1, 1, 3, 1, 9, 4, 5, 9, 1, 6, 5, 9, 3, 3, 4, 1, 8, 3, 3, 1, 2, 5, 1, 5, 5, 7, 3, 3, 9, 4, 3, 2, 7, 6, 4, 1, 4, 1, 5, 6, 9, 1, 1, 9, 5, 9, 5, 3, 4, 7, 9, 4, 4, 6, 5, 1, 4, 6, 6, 8, 7, 2, 6, 8, 8, 3, 4, 3, 1, 8, 4, 1, 5, 1, 5, 9, 7, 7, 9, 8, 1, 7, 4, 7, 1, 2, 1, 7, 2, 8, 5, 2, 3, 8, 8, 2, 6, 7, 6, 2, 9, 3, 3, 7, 4, 2, 8, 7, 3, 8, 5, 3, 5, 7, 9, 5, 6, 9, 9, 4, 5, 7, 5, 2, 6, 5, 1, 4, 9, 6, 1, 9, 5, 4, 2, 6, 1, 6, 7, 2, 9, 2, 9, 4, 6, 2, 4, 7, 8, 3, 9, 2, 2, 8, 8, 8, 3, 6, 5, 4, 3, 8, 7, 5, 1, 7, 3, 4, 3, 9, 7, 3, 1, 3, 8, 8, 2, 7, 8, 3, 5, 5, 4, 9, 3, 3, 8, 6, 2, 6, 9, 9, 8, 8, 3, 4, 6, 2, 2, 9, 6, 8, 6, 3, 3, 5, 7, 5, 3, 2, 2, 2, 6, 2, 1, 4, 4, 8, 6, 2, 4, 9, 9, 1, 6, 6, 6, 7, 7, 9, 6, 3, 1, 4, 1, 2, 6, 4, 5, 5, 6, 4, 5, 1, 5, 2, 8, 5, 4, 5, 1, 2, 9, 7, 4, 4, 2, 3, 5, 5, 7, 9, 8, 4, 4, 5, 4, 1, 4, 2, 1, 8, 6, 9, 8, 2, 7, 9, 8, 1, 7, 2, 4, 6, 4, 9, 6, 5, 7, 8, 1, 3, 5, 5, 2, 4, 6, 8, 9, 9, 9, 7, 6, 2, 1, 3, 4, 8, 7, 6, 5, 9, 9, 9, 6, 4, 4, 1, 9, 9, 6, 9, 5, 3, 3, 8, 6, 8, 8, 2, 4, 7, 2, 6, 5, 6, 1, 4, 1, 4, 5, 7, 7, 1, 9, 2, 7, 4, 4, 9, 1, 6, 2, 6, 9, 2, 1, 2, 8, 9, 9, 7, 1, 6, 3, 4, 4, 2, 7, 7, 2, 8, 8, 5, 2, 8, 5, 5, 5, 6, 5, 6, 2, 8, 1, 9, 4, 7, 7, 5, 8, 7, 2, 6, 7, 9, 3, 7, 9, 4, 2, 8, 7, 5, 2, 7, 2, 2, 7, 7, 9, 4, 2, 7, 1, 4, 8, 2, 8, 1, 4, 8, 1, 7, 8, 2, 6, 1, 3, 6, 3, 9, 2, 7, 8, 4, 2, 9, 1, 5, 2, 2, 3, 3, 3, 6, 5, 9, 9, 7, 2, 4, 8, 9, 5, 5, 8, 5, 8, 3, 4, 4, 6, 4, 7, 3, 6, 7, 2, 1, 9, 6, 8, 7, 8, 5, 3, 9, 1, 6, 1, 3, 3, 4, 2, 1, 3, 9, 3, 9, 6, 9, 5, 7, 4, 6, 6, 8, 7, 2, 5, 1, 6, 1, 8, 5, 7, 5, 6, 7, 2, 1, 6, 5, 3, 7, 9, 1, 8, 7, 2, 1, 7, 7, 3, 3, 3, 7, 8, 2, 2, 9, 1, 7, 5, 9, 3, 4, 8, 4, 4, 1, 8, 2, 5, 8, 1, 5, 6, 3, 7, 3, 1, 1, 1, 6, 7, 8, 3, 4, 2, 2, 9, 5, 4, 1, 6, 3, 8, 9, 2, 7, 5, 2, 3, 1, 9, 2, 4, 1, 3, 1, 2, 8, 2, 2, 5, 5, 5, 9, 8, 7, 2, 5, 5, 5, 5, 4, 1, 9, 5, 3, 5, 2, 8, 1, 2, 3, 6, 2, 3, 3, 9, 8, 2, 6, 7, 3, 9, 5, 6, 3, 2, 4, 9, 1, 1, 4, 2, 5, 3, 1, 7, 6, 4, 8, 6, 1, 5, 1, 7, 2, 6, 2, 1, 3, 3, 2, 9, 7, 6, 2, 7, 7, 4, 3, 6, 9, 9, 1, 2, 6, 5, 5, 2, 6, 3, 8, 7, 3, 8, 8, 5, 4, 2, 9, 4, 4, 6, 8, 5, 7, 3, 5, 8, 4, 8, 2, 2, 8, 5, 8, 8, 3, 9, 4, 2, 6, 3, 6, 7, 4, 3, 4, 4, 3, 7, 5, 8, 7, 3, 9, 4, 5, 2, 6, 2, 8, 6, 2, 6, 8, 9, 8, 3, 4, 6, 9, 6, 5, 8, 6, 1, 5, 8, 7, 2, 5, 8, 4, 1, 4, 7, 4, 8, 9, 6, 4, 6, 4, 8, 5, 6, 5, 4, 4, 6, 4, 7, 4, 4, 9, 4, 1, 7, 5, 6, 6, 5, 9, 9, 1, 4, 4, 3, 2, 3, 4, 2, 4, 4, 7, 3, 7, 1, 6, 7, 3, 8, 3, 6, 6, 2, 2, 1, 7, 1, 7, 8, 9, 3, 5, 3, 4, 4, 7, 3, 2, 7, 3, 4, 2, 1, 1, 8, 6, 5, 7, 8, 9, 6, 1, 2, 5, 8, 8, 9, 1, 3, 8, 6, 5, 8, 3, 8, 5, 6, 1, 7, 9, 2, 8, 1, 2, 3, 1, 6, 4, 1, 5, 4, 8, 8, 8, 3, 5, 3, 5, 3, 9, 9, 1, 2, 7, 8, 2, 8, 8, 7, 2, 7, 1, 6, 8, 3, 3, 6, 2, 8, 1, 5, 6, 6, 6, 3, 3, 3, 9, 2, 7, 5, 3, 6, 9, 9, 8, 2, 2, 8, 7, 6, 5, 8, 3, 6, 7, 4, 9, 4, 4, 7, 3, 2, 4, 1, 7, 5, 6, 2, 7, 6, 8, 1, 1, 6, 3, 3, 7, 9, 4, 1, 4, 4, 1, 5, 4, 6, 7, 6, 4, 8, 7, 1, 5, 6, 5, 6, 7, 6, 9, 1, 3, 4, 4, 2, 9, 2, 6, 9, 1, 8, 8, 5, 7, 2, 3, 3, 9, 9, 1, 1, 3, 3, 2, 1, 4, 3, 6, 2, 9, 3, 4, 3, 1, 6, 6, 2, 3, 4, 1, 9, 8, 1, 8, 6, 6, 8, 5]

# Write an expression to populate the `n_five` variable with the number of 5s ocurring in `list_of_int`.
n_five = list_of_ints.count(5)

#########################

################

# Mean, Median, and Mode
    # oftern used in machine learning

    # Mean - the average value

    # Median - the mid point value
        # must be ordered

    # Mode - the most commo value

### Mean - Average

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)

### Median - middle # (sorted)

#assorted set of number
    # needs to be ordered first before provding the median

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)


### Mode - value that appears the most
    # Use SciPy mode()
    

from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)
print(x)


### AI = gatherung infot hat you ahev and makign it an assumption with that


## standard deviation:
    # # that describes how spread out values are
        # low std deviation?
            # most of the numbers are close to the mean
        # high std dev
            # values are spread out over a wider range
# use NumPy std() method:

import numpy

speed = [86,87,88,86,87,85,86]

x = numpy.std(speed)
print(x)

## To create big data set for testing
    # use NumPy
        # comes with methods to create random data sets of any #

# create an array (list) containing 1000 random floats between 1 and 9:

import numpy

x = numpy.random.uniform(1.0,9.0,1000) # 1000 needs to be a whole number

print(x)

## create histograms

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0,0.5,250)

plt.hist(x,5) # how many bars there will be in the histogram
plt.show()


## create scatterplots

import matplotlib.pyplot as plt

# values of both x and y need to be of same quantity
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x,y)
plt.show()

#########################


