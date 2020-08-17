### Hamida July 22, 2020 ###

### Memory Test ###

### Question 1 ###
# create a list and assign it to my_list variable

my_list = [1, 2, 3]

# how many items are in the list?

    #Solution 1
        # use print function
print(len(my_list))

    #Solution 2
    # give a name to it e.g. x and then len and in bracket the variable name
x = len(my_list)

### Question 2 ###

dc_members = ["Superman", "Batman", "Wonder Woman", "Aquaman", "The Flash"]


# find the index of "Wonder Woman" in 'dc_members'
# set var to index

indx = dc_members.index("Wonder Woman")
print(indx)

### Question 3 ###

# add an item to a list


fav_animals = ["elephant", "dolphin", "tiger"]

# write an expression to add "shark" to the list

fav_animals.append("shark")
print(fav_animals)

### Question 4 ###

# write an expression to assign "caterpillar" to the 2nd item in the list

fav_animals[1] = "caterpillar" # 1 is  2nd spot in the line
print(fav_animals)

# insert the item in replacement of that 2nd item in the original list
fav_animals.insert(1, "caterpillar") # 1 is the 2nd spot in the line and inserting caterpillar to the list
print(fav_animals)

### Question 5 ###
fav_animals_2 = ["elephant", "dolphin", "tiger", "bee", "bird"]

# print Dolphin through bee
    # dolphin, tiger, and bee
    # call the variable range_animal

range_animal = fav_animals_2[1:4]
print(range_animal)

### Question 6 ###

# remove Elephant

    # Solution 1
        # when removing the value with "" quotes

fav_animals_2.remove("elephant")
print(fav_animals_2)

    # Solution 2
        # pop has index value
    
fav_animals_2.pop(0)
print(fav_animals_2)

    # Solution 3
        # del function 
del fav_animals_2[0]
print(fav_animals_2)

### Question 7 ###

# create a dictionary called aneesa_dict

# favorite color = green
# favorite car = honda
# favorite food = pizza
# favorite book = cats cradle

aneesa_dict = {
    
    "favorite color" : "green",
    "favorite car" : "honda",
    "favorite food" : "pizza",
    "favorite book" : "cats cradle"

    }

print(aneesa_dict)
