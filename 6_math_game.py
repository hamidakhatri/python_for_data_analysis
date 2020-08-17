# Ask for demographics

import time
print()
print("This is a survey.")
print()
print("Let's get started")
time.sleep(.1)
print()

def script():
    #get first name
    first_name = input("Enter your first name: ")
    print()

    #get last name
    last_name = input("Enter your last name: ")
    print()

    #get age
    age = input("Enter age: ")
    print()

    time.sleep(.2)
    print()

    time.sleep(.2)
    print("*--* *--* *--* *--*")
    print()
    print("<`)))< * <`)))< * <`)))<")
    print()
    print("*--* *--* *--* *--*")
    print()
    print("Let's celebrate!")
    print()
    print("  ___")
    print(" ('v')")
    print("((___))")
    print("   ^^  ")
    print()
    print("*--* *--* *--* *--*")
    print()
    time.sleep(.2)
    print()

    #play a game
    game1 = input("Would you like to play a game? ")
    if game1 == "yes" or game1 == "yeah" or game1 == "yep" or game1 == "y":
        print()

        def num_game():
            num1 = input("Enter 1st number: ")
            #convert text entered to a floating point number
            num1 = float(num1)

            time.sleep(.1)
            print()

            #get second number from the user
            num2 = input("Enter 2nd number: ")

            #convert text entered to a floating point number
            num2 = float(num2)
            print()

            #calculate and print the answer
            num3 = num1 + num2
            print("The total is: ",num3)

            print()
            print("*--* *--* *--* *--*")
            print()
            print("Let's celebrate!")
            print()
            print("\('_')")
            print("  )))z")
            print("  //")
            print()
            print("*--* *--* *--* *--*")
            print()

            game2 = input("Would you like to continue? ")
            if game2 == "yes" or game2 == "yeah" or game2 == "yep" or game2 == "y":
                print()
                num_game()

            if game2 == "no" or game2 == "nope" or game2 == "na" or game2 == "n":
                print()
                print("That was the end of our journey together!")

        num_game()

        
    if game1 == "no" or game1 == "nope" or game1 == "na" or game1 == "n":
        print()
        print("*--* *--* *--* *--*")
        print()
        print("No problem. Thank you for being with us this far.")
        print()
        time.sleep(.1)
        print("*--* *--* *--* *--*")

script()
