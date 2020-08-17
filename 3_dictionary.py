## By
## Hamida Khatri


## HOMEWORK PRACTICE ##
# due Mon 7/13/20 @ 5:45pm)
##### To create a dictionary of our own with at least 10 items:
    ## add an item to the dict (totaling 11 items)
    ## remove an item (totaling 9 items)
    ## change an item


# adding time delays
import time


##### CREATING A DICTIONARY FOR COLORS OF EMOTIONS #####")

print()
print()

print("##### DICTIONARY OF EMOTIONS #####")

print()
print()

print("Main Dictionary with 10 Items")

print()
      
# we use "{" to begin and "}" to end the dictionary
dictionary_emotions = {
    
    # (left side) key : (right side) value -> both are resting within '""' quotation marks
    # list of keys as the color and values representing the emotion associated with the color
    # we itemize the list one row at a time with "," in the end
    "Red" : "Anger",
    "Blue" : "Calm",
    "Yellow" : "Happiness",
    "Green" : "Envy",
    "Purple" : "Pride",
    "Gray" : "Sadness",
    "Black" : "Power",
    "Pink" : "Cheerful",
    "White" : "Innocence",
    "Teal" : "Spritual",
    }

# printing the main dictionary of emotions
print(dictionary_emotions)

# adding visual space
print()
print()

print("Main Itemized Key List")

print()
      
# printing all key items in the list
for x in dictionary_emotions:
    print(x)

# adding visual space
print()

# printing the length of the dictionary
print("Dictionary Length:")
print(len(dictionary_emotions))

# time delay to read the output
time.sleep(3)

##### ADDING AN ITEM TO THE DICTIONARY OF EMOTIONS #####

# adding visual space
print()
print()

print("Updated Dictionary with 11 Items")

print()

# use "[]" to add the new key to the dictionary and assigning the value in '""' quotes
dictionary_emotions["Brown"] = "Resilience"

# printing the dictionary of emotions
print(dictionary_emotions)

print()

print("Updated Itemized Key List")

print()

# printing the updated keys in the dictionary
for x in dictionary_emotions:
    print(x)

# adding visual space
print()

# printing the length of the updated dictionary
print("Dictionary Length:")
print(len(dictionary_emotions))

# time delay to read the output
time.sleep(3)

##### REMOVING ONE ITEM BY INDEX FROM THE DICTIONARY OF EMOTIONS #####

# adding visual space
print()
print()

print("Updated Dictionary with 10 Items")

print()

# use "pop" to remove an item from the dictionary by putting the index value in "()"
dictionary_emotions.pop("Purple")

# printing the dictionary of emotions
print(dictionary_emotions)

print()

print("Updated Itemized Key List")

print()

# printing the updated keys in the dictionary
for x in dictionary_emotions:
    print(x)

# adding visual space
print()

# printing the length of the updated dictionary
print("Dictionary Length:")
print(len(dictionary_emotions))

# time delay to read the output
time.sleep(3)

##### DELETING ONE ITEM FROM THE DICTIONARY OF EMOTIONS #####

# adding visual space
print()
print()

print("Updated Itemized Key List with 9 Items")

print()

# use "del" and assign the key in "[]" to delete it from the dictionary 
del dictionary_emotions["White"]

# printing the dictionary of emotions
print(dictionary_emotions)

print()

print("Updated Itemized Key List")

print()

# printing the updated keys in the dictionary
for x in dictionary_emotions:
    print(x)

# adding visual space
print()

# printing the length of the updated dictionary
print("Dictionary Length:")
print(len(dictionary_emotions))

# time delay to read the output
time.sleep(3)

##### CHANGING/UPDATING AN ITEM FROM THE DICTIONARY OF EMOTIONS #####

# adding visual space
print()
print()

print("Updated Itemized Key List with 9 Items")

print()

# put the key that needs to be updated in "[]" and the value that needs to be changed into in '""' quotes
dictionary_emotions["Yellow"] = "Confident"


# printing the dictionary of emotions
print(dictionary_emotions)

print()

print("Updated Itemized Key List")

print()

# printing the updated keys in the dictionary
for x in dictionary_emotions:
    print(x)

# adding visual space
print()

# printing the length of the updated dictionary
print("Dictionary Length:")
print(len(dictionary_emotions))
