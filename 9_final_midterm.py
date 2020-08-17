import datetime
import math
import time
import random
import numpy
from scipy import stats


print("This is a mth function game.")

print()
time.sleep(0.5)


def datagame():

    # min number from user from 1-10 (not including 1 and 10)
    minimum_number = 0
    while 1 >= minimum_number or 10 <= minimum_number:
        minimum_number = float(input("Please enter a minimum number between 1-10: "))

    time.sleep(0.5)
    print()

    # max number from user from 400-500 (inclduing 400 and 500)
    maximum_number = 0
    while 400 > maximum_number or 500 < maximum_number:
        maximum_number = float(input("Please enter a maximum number betwen 400-500: "))

    time.sleep(0.5)
    print()

    # create the list of 50 random numbers within user specified range
    dataset = numpy.random.uniform(float(minimum_number), float(maximum_number), 50)
    print("The list is:", dataset)

    print()
    time.sleep(0.5)

    v = numpy.mean(dataset)
    print("The mean is: ", v)

    print()
    time.sleep(0.5)
    
    y = numpy.median(dataset)
    print("The median is: ", y)

    print()
    time.sleep(0.5)
    
    z = stats.mode(dataset)
    print("The standard deviation is: ", z)

    print()
    time.sleep(0.5)
    
    # print file
    print_to_file = input("Do you want to print all of your answers into a text file? Yes/No ")
    print()
    if print_to_file.lower() == "yes":
        # creating the file
        f = open("midterm.txt", "x")
        # writing to the file
        f = open("midterm.txt", "w")
        f.write("Mean: ")
        f.write(str(v))
        f.write("\nMedian: ")
        f.write(str(y))
        f.write("\nThe standard deviation is: ")
        f.write(str(z))
        f.close()
    if print_to_file.lower() == "no":
        print("Goodbye!")

    print()
    time.sleep(0.5)

    # restart function
    def res():
        restart = input("Do you want to create another data set? Yes/No ")
        print()
        if restart.lower() == "yes" or restart == "Yes":
            datagame()
        elif restart.lower() == "no" or restart == "No":
            print("Goodbye!")
        else:
            print("I did not understand that.")
            res()
            print()
    res()
        
    time.sleep(0.5)

datagame()
