#adds the library to allow us to use time delays
import time

#function to ask Julia questions
def julia():
  #say hello
  print("Hello, Julia! I'd like to learn more about you!")

  #ask the user to enter a response
  familiarity = input("Are you familiar with Python, Julia? ")

  #evaluate whether the response is affirmative or negative (if, elif, else)
  if familiarity == "yes" or familiarity == "yeah" or familiarity == "y":
    #prints the statement in quotes on the screen
    print("That's awesome!!")
    #wait a half-second
    time.sleep(0.5)
    #prints the statement in quotes on the screen
    print("I am a beginner myself. I only know a bit of SQL and HTML.")
    #wait a half-second
    time.sleep(0.5)
    #prints the statement in quotes on the screen
    print("I heard you say, you know C++." )
  elif familiarity == "no" or familiarity == "nah" or familiarity == "n":
    #prints the statement in quotes on the screen
    print("No problem. I am a beginner myself.")
  else:
    #prints the statement in quotes on the screen
    print("Hmm, I didn't understand that. Let's move on.")

  #wait a half second
  time.sleep(0.5)
  #print() outputs a blank space
  print()
  
  #ask the user to enter a response
  color = input("What is your favorite color? ")
  #wait a half second
  time.sleep(0.5)
  print()

  #create an empty list
  countries = []
  #ask the user to enter a response
  travel = input("What is the first country that you have visited? ")
  #wait a half second
  time.sleep(0.5)
  #prints the statement in quotes on the screen
  print("Oh, I have been there too.")
  print()
  #add the response to the list of countries
  countries.append(travel)
  #ask the user to enter a response
  travel = input("What is the second place you have visited?: ")
  #wait a half second
  time.sleep(0.5)
  #prints the statement in quotes on the screen
  print("That's great!")
  #add the response to the list of countries
  countries.append(travel)
  #prints the statement in quotes on the screen
  print("Let me recap.")

  #print each items in the list of countires
  for y in countries:
    print(y)

#function to ask Hamida questions
def hamida():
  #say hello
  print("Hello, Hamida! I'd like to learn more about you!")
  #wait a half second
  time.sleep(.5)

  #ask user for input
  favcolor = input("What is your favorite animal? ")
  #wait a half-second
  time.sleep(.5)
  #evaluate the response to see if it matches "cat" or "cats"
  if favcolor == "cat" or favcolor == "cats":
    print("Cool, cats are also my favorite animal!")
  else:
    print("Oh, nice! I like",favcolor,"too, but cats are my personal favorite.")
  
  #create an empty list
  languages = []
  
  #print an empty line
  print()

  #ask user for input
  response = input("What's one language that you know, Hamida? ")
  
  #add the response to the list of languages
  languages.append(response)
  
  #wait a half-second
  time.sleep(.5)
  
  #print the response and ask if there are more languages
  print("Cool, you know "+response+"?! That's awesome!")
  
  #wait a half-second
  time.sleep(.5)
  #print an empty line
  print()

  #ask user for input
  response = input("What's another language you know? ")
  #add the response to the list of languages
  languages.append(response)
  #wait a half-second
  time.sleep(.5)
  #print the response and ask if there are more languages
  print("Wow, that's so interesting that you know "+response+".")
  #wait a half-second
  time.sleep(.5)
  #print an empty line
  print()

  #ask user for input
  response = input("What's one more language you know? ")
  #add the response to the list of languages
  languages.append(response)
  #wait a half-second
  time.sleep(.5)
  #print the response
  print("Wow,",response+", that's so cool!")
  #wait one second
  time.sleep(1)
  
  #print an empty line
  print()
  print("So, let me get this straight. These are some of the languages you know:")
  #print each item in the list of languages
  for x in languages:
    print(x)


#call the function to ask Julia questions
julia()
#wait one second
time.sleep(1)
#print a blank line to the screen
print()
#call the function to ask Hamida questions
hamida()
  
