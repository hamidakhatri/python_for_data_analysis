# WEDNESDAY, JUL 1 2020

#For your reference:
    #TEST YOUR MEMORY:
    #How do you write a piece of code simply asking the user for their name, and then saying "Hi, name" ?

#long way
print("Good evening. What is your name?")
variable = input('Enter your name: ') 
print("Hello, " + variable)

#shorthand
name = input('What is your name?\n')
print ('Hi, %s.' % name)

####################################
#Homework:
    #Why the extra punctuation?
    ##They are used for formatting the text or performing operations

    #What does it mean?
      ##"\" is called "escape" it means whitespace character
        ##"\n" means new line
        ##other examples are "\t" for tab and "\r" for return
      ##"%" does two things:
        ##"%s" is a format specifier that tells Python to format the text where "s" represents string
        ##"%" is a modulo (math) operator when the arguments are number and it returns the remainder of the numerator divided by the denominator

    ##What if you replace 's' with another letter?
      ##I tried replacing "%s" with "%d" where I discovered that "d" represents number and prints it out as is
      ##for example:
age = input("What is your age?\n")
print ("That is good to know. I am %d years old." % 5)

####################################


#For your reference:
    #while loop: execute a set of statements as long as a condition is true
    #Print i as long as i is less than 6
i = 1
while i < 6:
  print(i)
  i += 1
  
#increment i, or loop will continue forever (not good)

####################################
#Homework:
    #Why the letter 'i'?
      ##"i" is iteration. In othere words it is a variable. It can be replaced by anything you want to call it.
        ##for example I replaced "i" with "number":
          ##number = 1
            ##while number < 6:
              ##print(number)
              ##number += 1
  
    #Why the '+='?
      ##"+=" represents adding the number after it to the variable, in the example 1 is added to variable "i" until it reaches the last number that is less than 6, in this case it will be 5
  
    #What does it mean?
      ##"+=" adds a number to a variable. In other words, an increment to the variable with whatever number you mention after "+="
  
    #What happens if you replace 'i' with another letter?
      ##"i" is iteration. In othere words it is a variable. It can be replaced by anything you want to call it. Just like the example mentioned above.
  
####################################


#For your reference:
    #math.ceil()
        #rounds a num up to nearest int
    #math.floor()
        #rounds a num down to nearest int

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) #returns 2
print(y) #returns 1



######################################
#Homework:
    #What happens if you don't enter a decimal? i.e. 10?
      ##it returns the whole number 10 if 1.4 is replaced by 10

    #What happens if I enter a number typed out? i.e. ten?
      ##it will give a syntax error that name 'ten' is not defined

######################################


#For your reference:
    #RegEx in Python
        #Example: Search the string to see if it starts with "The" and ends with "Spain"
        #Check if the string starts with "The" and ends with "Spain":

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES, We have a match!")
else:
  print("No match")


##########################################
'''
HOME PRACTICE:
https://www.w3schools.com/python/python_regex.asp

Write a regex for finding a piece of info in a large body of text.

'''

import re
  
story = """Many years ago the hippopotamus, whose name was Isantim, was one of the biggest kings on the land; he was second only to the elephant. The hippo had seven large fat wives, of whom he was very fond. Now and then he used to give a big feast to the people, but a curious thing was that, although everyone knew the hippo, no one, except his seven wives, knew his name.
At one of the feasts, just as the people were about to sit down, the hippo said, "You have come to feed at my table, but none of you know my name. If you cannot tell my name, you shall all of you go away without your dinner." As they could not guess his name, they had to go away and leave all the good food and tombo behind them. But before they left, the tortoise stood up and asked the hippopotamus what he would do if he told him his name at the next feast. So the hippo replied that he would be so ashamed of himself, that he and his whole family would leave the land, and for the future would dwell in the water. Now it was the custom for the hippo and his seven wives to go down every morning and evening to the river to wash and have a drink. Of this custom the tortoise was aware. The hippo used to walk first, and the seven wives followed. One day when they had gone down to the river to bathe, the tortoise made a small hole in the middle of the path, and then waited. When the hippo and his wives returned, two of the wives were some distance behind, so the tortoise came out from where he had been hiding, and half buried himself in the hole he had dug, leaving the greater part of his shell exposed. When the two hippo wives came along, the first one knocked her foot against the tortoise's shell, and immediately called out to her husband, "Oh! Isantim, my husband, I have hurt my foot." At this the tortoise was very glad, and went joyfully home, as he had found out the hippo's name. When the next feast was given by the hippo, he made the same condition about his name; so the tortoise got up and said, "You promise you will not kill me if I tell you your name?" and the hippo promised. The tortoise then shouted as loud as he was able, "Your name is Isantim," at which a cheer went up from all the people, and then they sat down to their dinner. When the feast was over, the hippo, with his seven wives, in accordance with his promise, went down to the river, and they have always lived in the water from that day till now; and although they come on shore to feed at night, you never find a hippo on the land in the daytime."""

#"[]" used to find a set of characters, in this case "Hippo"
hword1 = re.findall("[Hippo]", story)
if hword1:
  print("Yes, we have numerous matches!")
else:
  print("None found.")

#to print/find a list of all matches for the word "hippo"
hword2 = re.findall("hippo", story)
print(hword2)

#to find if there is text that begins with "Many" in a large body of text
#"^" is used for the start of the character
lookup1 = re.search("^Many", story)

if lookup1:
  print("Yes, we have atleast one match!")
else:
  print("None found.")

#to find if there is text that ends with "daytime." in a large body of text
#"$" is used for the end of the character
lookup2 = re.search("daytime.$", story)

if lookup2:
  print("Yes, we have atleast one match!")
else:
  print("None found.")

##########################################
