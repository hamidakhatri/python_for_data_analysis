#Individual Midterm Practice
#Monday August 3rd 2020

#This is to be treated like a midterm.
#You should work on these tasks utilizing your cheatsheet that you should have created already

#Your task:
  #Create a User Program that creates a bunch of options for the user and allows them to pick what option they want. This program must be able to rerun/restart if a user enters "invalid" info.
  #I will outline __ tasks. Complete as many tasks as you are able to.
  #You should think of wrapping up ~8:00p

#Tasks include...

  #1: Data Game
    #Allow the user to pick a min and max number
    #Create a data set (array) within user's specified range
    #Give the user THREE options of data manipulation (i.e. mean/median/mode/standard dev)
  
  #2: Basic Math Game
    #reqs: addition, subtraction, square root, division, multiplication, displaying min/max numbers in any given list, manipulating data in other ways from a list
  
  #3: Get to know a friend
    #Audience: working, non-technical professionals
    #Should be a game made for two people to play to get to know a little more about the other
    #Must find a way to learn 10 things about the partner, and save that information into a text file.
  
  #4: File Usage!
    #The program must be able to...
      #Create a new empty txt file in user's directory
      #Add a line of info to the above new file
      #Re-print the contents of the file
      #Add another line to the txt file
      #and repeat!
        #what should the lines in the txt file say? This txt file can be informational or funny, once it's neat and organized.
  
  #***5: List/Dictionary Creation:
    #*** Create a list/dictionary of your choice
    #*** Work with the user to display certain items in the list/dictionary
    #*** Completely up to you - be creative!

#Again, only include the amount of tasks you are able to complete.
# Complete tasks to YOUR understanding of what I am asking


### Individual Review ###
  
### MidTerm ###

### 3 August, 2020 ###

# import all modules

import datetime
import time
import random
import numpy
import math
from scipy import stats

# time date
datetime_object = datetime.datetime.now()
print(datetime_object)
print()
time.sleep(0.5)

# intro function
def introduction():
    title = "### Welcome. Let's Play A Game. ###"
    print("*" * len(title))
    print(title)
    print("*" * len(title))
    print()
    time.sleep(0.5)
    print("Main Menu")
    time.sleep(0.25)
introduction()

print()
time.sleep(0.5)

def user_program():
        
    def display_menu():
        menu_list = ["1. Data Game", "2. Basic Math", "3. Get To Know You", "4. File Usage", "5. List", "6. Exit the Game"]
        print(menu_list[0])
        time.sleep(0.25)
        print(menu_list[1])
        time.sleep(0.25)
        print(menu_list[2])
        time.sleep(0.25)
        print(menu_list[3])
        time.sleep(0.25)
        print(menu_list[4])
        time.sleep(0.25)
        print(menu_list[5])
        print()
        time.sleep(0.25)
    display_menu()

#1. Data Game

    #Allow the user to pick a min and max number
    #Create a data set (array) within user's specified range
    #Give the user THREE options of data manipulation (i.e. mean/median/mode/standard dev)

    ### GAME 1 - Data Game
    game_choice_selection = input("Select your option: ")
    print()
    
    if game_choice_selection == "1":

        def data_game_title():
            data_game = "### Data Game ###"
            print("*" * len(data_game))
            print(data_game)
            print("*" * len(data_game))
            print()
            time.sleep(0.25)
        data_game_title()

        def min_max():
            user_input_min = int(input("Enter the 1st number of your choice: "))
            time.sleep(.1)
            print()
            user_input_max = int(input("Enter the 2nd number of your choice that is larger than the 1st number you entered earlier: "))
            print()
            dataset = numpy.random.uniform(int(user_input_min), int(user_input_max), 12)
            time.sleep(0.25)
            print("Here is the dataset that we have collected " + str(dataset))
            time.sleep(0.25)
            print()

            # Choice Menu
            def choice_loop():
                    
                time.sleep(0.25)
                choice = input("Would you like to know the mean, median, or mode for the dataset? \n\nPlease select from the Choice Menu:\n\nA: Mean \nB: Median \nC: Mode \n\nEnter your choice: ")
                print()
                if choice == "A" or choice == "mean" or choice == "a":
                    print("The mean is " + str(numpy.mean(dataset)))
                    time.sleep(0.25)
                elif choice == "B" or choice == "median" or choice == "b":
                    print("The median is " + str(numpy.median(dataset)))
                    time.sleep(0.25)
                elif choice == "C" or choice == "mode" or choice == "c":
                    print("The mode is " + str(stats.mode(dataset)))
                    time.sleep(0.25)
                else:
                    print("Hmm... I don't quite understand. Let's try again.")
                    print()
                    time.sleep(0.25)
                    
                    # Creating the Main Restart function
                    def main_restart_function():
                        main_restart = input("Would you like to go to the Main Menu? y/n ")
                        print()
                        if main_restart == "y":
                            user_program()
                        elif main_restart == "n":
                            print("Thanks for playing!\n")
                            user_program()
                        else:
                            print("Hmm... I don't quite understand. Let's try again.")
                            user_program()
                    main_restart_function()
                    
                
                ## Go back to the Choice Menu to select other options
                def choice_restart_function():
                    print()
                    choice_restart = input("Let's go back to the Choice Menu? y/n ")
                    print()
                    if choice_restart == "y":
                        choice_loop()
                    elif choice_restart == "n":
                        print("Thanks for playing!")
                    else:
                        print("Invalid entry.")
                choice_restart_function()

                print()
                time.sleep(0.25)

            choice_loop()

            # Creating the Main Restart function
            def main_restart_function():
                main_restart = input("Would you like to go to the Main Menu y/n ")
                print()
                if main_restart == "y":
                    user_program()
                elif main_restart == "n":
                    print("Thanks for playing!\n")
                    user_program()
                else:
                    print("Hmm... I don't quite understand. Let's try again.")
                    user_program()
            main_restart_function()

        min_max()


#2: Basic Math Game
    #reqs: addition, subtraction, square root, division, multiplication, displaying min/max numbers in any given list, manipulating data in other ways from a list
    ## GAME 2 - Basic Math

    if game_choice_selection == "2":

      def basic_math():
        basic_math_title = "### Basic Math ###"
        print("*" * len(basic_math_title))
        print(basic_math_title)
        print("*" * len(basic_math_title))
        print()
        time.sleep(0.25)
      basic_math()
      
      time.sleep(0.25)

    ## created a loop to run the menu again! YAY!! Figured it out after so many failure runs!
      def math_loop():

          def math_game_menu():
              print("Basic Math Menu \n\nSelect your choice to start: \n")
              math_game_menu_list = ["I. Addition", "II. Subtraction", "III. Square Root", "IV. Division", "V. Multiplication", "VI. Minimum and Maximum"]
              print(math_game_menu_list[0])
              time.sleep(0.25)
              print(math_game_menu_list[1])
              time.sleep(0.25)
              print(math_game_menu_list[2])
              time.sleep(0.25)
              print(math_game_menu_list[3])
              time.sleep(0.25)
              print(math_game_menu_list[4])
              time.sleep(0.25)
              print(math_game_menu_list[5])
              print()
          math_game_menu()

          math_game_choice = input("Select your option: ")
          print()

        ## Addition
          if math_game_choice == "I" or math_game_choice == "i":
              
              def one_add():

                  a = int(input("Enter the 1st number that you wish to add: "))
                  print()
                  time.sleep(0.25)
                  b = int(input("Enter the 2nd number that you wish to add: "))

                  ans = int(a) + int(b)
                  print()
                  time.sleep(0.25)
                  print("The sum of the numbers is: ", ans)

              one_add()

        ## Subraction
          if math_game_choice == "II" or math_game_choice == "ii":
              
              def two_sub():

                  a = int(input("Enter the 1st number that you wish to subtract: "))
                  print()
                  time.sleep(0.25)
                  b = int(input("Enter the 2nd number that you wish to subtract: "))

                  ans = int(a) - int(b)
                  print()
                  time.sleep(0.25)
                  print("The difference of the numbers is: ", ans)

              two_sub()

        ## Square Root
          if math_game_choice == "III" or math_game_choice == "iii":
              
              def three_sqrt():

                  a = int(input("Enter the number you wish to find the square root of: "))

                  ans = math.sqrt(int(a))
                  print()
                  time.sleep(0.25)
                  print("The square root of the number is: ", ans)

              three_sqrt()

          if math_game_choice == "IV" or math_game_choice == "iv":
              
              def four_div():

                  a = int(input("Enter the dividend: "))
                  print()
                  time.sleep(0.25)
                  b = int(input("Enter the divisor: "))
                  
                  ans = int(a) / int(b)
                  print()
                  time.sleep(0.25)
                  print("The quotient is: ", ans)

              four_div()

        ## Multiplication              
          if math_game_choice == "V" or math_game_choice == "v":
              
              def five_mul():

                  a = int(input("Enter the 1st number that you wish to multiply: "))
                  print()
                  time.sleep(0.25)
                  b =int(input("Enter the 2nd number that you wish to multiply: "))
                  
                  ans = int(a) * int(b)
                  print()
                  time.sleep(0.25)
                  print("The product of the numbers is: ", ans)

              five_mul()

        ## Minimum Maximum
          if math_game_choice == "VI" or math_game_choice == "vi":
              
              def six_minmax():

                  a = int(input("Enter the 1st number that you wish to start your number list with: "))
                  print()
                  time.sleep(0.25)
                  b = int(input("Enter the 2nd number that you wish to end your number list with: "))

                  list = numpy.random.uniform(int(a), int(b), 10)
                  print()
                  time.sleep(0.25)
                  print("Here is the generated list of random numbers:")
                  print(list)
                  print()
                  time.sleep(0.25)

                  print("Let us now calculate the minimum from the list:")
                  print()
                  time.sleep(0.5)
                  print(min(list))
                  print()
                  
                  print("Let us now calculate the maximum from the list:")
                  print()
                  time.sleep(0.5)
                  print(max(list))

              six_minmax()

              print()
              time.sleep(0.25)

        ## Go back to the Basic Math Menu to run other required functions
          restart = input("\nLet's go back to the Basic Math Menu? y/n ")
          print()
          if restart == "y":
              math_loop()
          if restart == "n":
              print("Thanks for playing!")

              print()
              time.sleep(0.25)

              # Creating the Main Restart function
              def main_restart_function():
                  main_restart = input("Would you like to go to the Main Menu? y/n ")
                  print()
                  if main_restart == "y":
                      user_program()
                  elif main_restart == "n":
                      print("Thanks for playing!\n")
                      user_program()
                  else:
                      print("Hmm... I don't quite understand. Let's try again.")
                      user_program()
              main_restart_function()

      math_loop()


#3: Get to know a friend
    #Audience: working, non-technical professionals
    #Should be a game made for two people to play to get to know a little more about the other
    #Must find a way to learn 10 things about the partner, and save that information into a text file.

    ## GAME 3 - Get to know a friend    

    if game_choice_selection == "3":

        def gettoknowyou():
            gettoknowyou_title = "### Get To Know You ###"
            print("*" * len(gettoknowyou_title))
            print(gettoknowyou_title)
            print("*" * len(gettoknowyou_title))
            print()
            time.sleep(0.25)
        gettoknowyou()

        time.sleep(0.25)

        name = input("Hello! What is your name? ")
        print("\nNice to meet you, " + name + " . \n\nMy name is Hamida. \n\nLet's get to know each other better. \n\nI am going to ask you some questions and respond to you with my answers to them. \n\nLet's get started!")

        def friend():
            # creating the file
            f = open("friend.txt", "x")
            # writing to the file
            f = open("friend.txt", "w")
            f.write("Facts about " + name + " and Hamida!\n\n")
            f.close()

            # appending to the file
            f = open("friend.txt", "a")
            age = str(input("\nWhat is you age? "))
            f.write("\nQuestion 1: What is your age?\n")
            f.write(age)
            f.write("\nI am 35 years old.\n")
            time.sleep(0.25)
            f.close()

            f = open("friend.txt", "a")
            color = str(input("\nWhat is your favorite color? "))
            f.write("\nQuestion 2: What is your favorite color?\n")
            f.write(color)
            time.sleep(0.25)
            f.write("\nMine is yellow!\n")
            f.close()

            f = open("friend.txt", "a")
            travel = str(input("\nWhat is the first country that you have visited? "))
            f.write("\nQuestion 3: What is the first country that you have visited?\n")
            f.write(travel)
            time.sleep(0.25)
            f.write("\nOh, I have been there too.\n")
            f.close()

            f = open("friend.txt", "a")
            travel2 = input("\nWhat is the second place you have visited?: ")
            f.write("\nQuestion 4: What is the second place you have visited?\n")
            f.write(travel2)
            time.sleep(0.25)
            f.write("\nThat's great! I have visited India as my second place in the list.\n")
            f.close()

            f = open("friend.txt", "a")
            animal = str(input("\nWhat is your favorite animal? "))
            f.write("\nQuestion 5: What is your favorite animal?\n")
            f.write(animal)
            time.sleep(0.25)
            f.write("\nI love cats!\n")
            f.close()

            f = open("friend.txt", "a")
            language = str(input("\nWhat's one language that you know? "))
            f.write("\nQuestion 6: What's one language that you know?\n")
            f.write(language)
            f.write("\nCool, you know " + language +"?! That's awesome!")
            time.sleep(0.25)
            f.write("\nI know Urdu.\n")
            f.close()

            f = open("friend.txt", "a")
            language2 = str(input("\nWhat's another language you know? "))
            f.write("\nQuestion 7: What's another language you know?\n")
            f.write(language2)
            f.write("\nWow, that's so interesting that you know " + language2 + ".")
            time.sleep(0.25)
            f.write("\nI also known a little bit of French.\n")
            f.close()

            f = open("friend.txt", "a")
            run = str(input("\nDo you like to run? "))
            f.write("\nQuestion 8: Do you like to run?\n")
            f.write(run)
            f.write("\nMe too!\nI go for a run outside my apartment every evening.\n")
            f.close()

            f = open("friend.txt", "a")
            food = str(input("\nWhat is your favorite food? "))
            f.write("\nQuestion 9: What is your favorite food?\n")
            f.write(food)
            f.write("\nThat's awesome. I lurrrrrvvvv pasta!\n")
            time.sleep(0.25)
            f.close()
        friend()
        
        time.sleep(0.25)
        print()

        # Creating the Main Restart function
        def main_restart_function():
            main_restart = input("Would you like to go to the Main Menu? y/n ")
            print()
            if main_restart == "y":
                user_program()
            elif main_restart == "n":
                print("Thanks for playing!\n")
                user_program()
            else:
                print("Hmm... I don't quite understand. Let's try again.")
                user_program()
        main_restart_function()
        

#4: File Usage!
    #The program must be able to...
      #Create a new empty txt file in user's directory
      #Add a line of info to the above new file
      #Re-print the contents of the file
      #Add another line to the txt file
      #and repeat!
        #what should the lines in the txt file say? This txt file can be informational or funny, once it's neat and organized.

    ## GAME 4 - File Usage   

    if game_choice_selection == "4":

        def fileusage_title():
            basic_math_title = "### File Usage ###"
            print("*" * len(basic_math_title))
            print(basic_math_title)
            print("*" * len(basic_math_title))
            print()
            time.sleep(0.25)
        fileusage_title()

        time.sleep(0.25)

        def file_usage():
        # creating the file
            f = open("newfile.txt", "x")

        # writing to the file
            f = open("newfile.txt", "w")
            f.write("## Facts About Pakistan ##\n")
            f.write("Pakistan, populous and multiethnic country of South Asia. \nHaving a predominately Indo-Iranian speaking population, Pakistan has historically and culturally been associated with its neighbours Iran, Afghanistan, and India. \nSince Pakistan and India achieved independence in 1947, Pakistan has been distinguished from its larger southeastern neighbour by its overwhelmingly Muslim population (as opposed to the predominance of Hindus in India).\n")
            f.close()

            # print file
            f.close()
            f = open ("newfile.txt", "r")
            for x in f:
                print(x)

            # add a line (append)
            f = open("newfile.txt", "a")
            f.write("\nPakistan is one of the largest producers of cotton.\n")
            f.close()

            # repeat by adding another line (append)
            f = open("newfile.txt", "a")
            f.write("\nPakistan has a mine for natural minerals but it is untapped.\n")
            f.close()

            # Creating the Main Restart function
            def main_restart_function():
                main_restart = input("Would you like to go to the Main Menu? y/n ")
                print()
                if main_restart == "y":
                    user_program()
                elif main_restart == "n":
                    print("Thanks for playing!\n")
                    user_program()
                else:
                    print("Hmm... I don't quite understand. Let's try again.")
                    user_program()
            main_restart_function()

        file_usage()

#***5: List/Dictionary Creation:
    #*** Create a list/dictionary of your choice
    #*** Work with the user to display certain items in the list/dictionary
    #*** Completely up to you - be creative!           
       
    ## GAME 5 - List   

    if game_choice_selection == "5":

        def list_title():
            listtitle_title = "### List ###"
            print("*" * len(listtitle_title))
            print(listtitle_title)
            print("*" * len(listtitle_title))
            print()
            time.sleep(0.25)
        list_title()

        time.sleep(0.25)

        def emotion_list():

            print("##### List of Emotions #####")
            print()
                  
            emo_list = []

            print("Let's add the different emotions in the list. ")
            print()
            time.sleep(0.25)

            emo1 = str(input("What is your favorite emotion? "))
            print()
            time.sleep(0.25)

            emo_list.append(emo1)

            emo2 = str(input("What is your second favorite emotion? "))
            print()
            time.sleep(0.25)

            emo_list.append(emo2)

            emo3 = str(input("Let's add two more, please? "))
            print()
            time.sleep(0.25)

            emo_list.append(emo3)

            print("Now let's print the items that are added to the list: ")
            print()
            time.sleep(0.25)
            
            print(emo_list)
            
            print()
            time.sleep(0.25)


            # Creating the Main Restart function
            def main_restart_function():
                main_restart = input("Would you like to go to the Main Menu? y/n ")
                print()
                if main_restart == "y":
                    user_program()
                elif main_restart == "n":
                    print("Thanks for playing!\n")
                    user_program()
                else:
                    print("Hmm... I don't quite understand. Let's try again.")
                    user_program()
            main_restart_function()
                       
        emotion_list()


    ## OPTION 6 - Exit   

    if game_choice_selection == "6":


        def exit_game():
            title = "### Exit Game ###"
            print("*" * len(title))
            print(title)
            print("*" * len(title))
            print()
            time.sleep(0.25)
            print("Thank you for playing!")
            time.sleep(0.25)
            print()
            time.sleep(0.25)
        exit_game()

        def exit_title():
            e_title = "### THE END ###"
            print("*" * len(e_title))
            print(e_title)
            print("*" * len(e_title))
            print()
            time.sleep(0.25)
        exit_title()
            

user_program()
