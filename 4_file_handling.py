# folder in documents
    #wed july 15




# py file
    #classjuly15




## File handling in Python

    # files in python: opne()
        # filename
        # mode (outlinging what you want python to do to that file)

        # 4 modes:

            # r - read default(val)
                # opens a file of reading
                # error if the file does not exist

            # a - append
                # opens a file for appending
                # adding information right beleow the last peice of information
                # created the file if it does not exist

            # w - write
                # pens a file for writing
                # oevrwriting the file
                # file exists, all content is erased and replaced
                # you cant get  teh unfo back when you overwrite the file
                # creates the file if it does not exist

            # x - create
                # why would you overwrite the file when you can create the file
                # dont prefer to delete the file
                # creates the specifide file
                # returns an error if the file already exists



# speicify if file should be handled as: binary / text
    # t - text - default valye - text mode
    # b - binary - bninary mode (images etc)



#since both r and t are default values, no need to specify
    # if you forgot to read the file, it will automatically do that
    # if you want to append it, it will not do it and put a for that



## OPENING FILES

    #** must be saved in teh same file directory as your .py file is saved
        # open() function (built-in)
        # contain a read() method to read and display contents of file

f = open ("july15txtfile.txt", "r")
print(f.read())


    #file located in a different location?

    # specify the file path:

f = open ("/Users/hami-k/Documents/wedjuly15/july15txtfile.txt", "r")
print(f.read())



# text file name:
    #july15txtfile.txt




# Default - read() method returns entire text
    # specify how many characters?
# return the 5 first characters of the file

f = open ("july15txtfile.txt", "r")
print(f.read(5))




## return on line
    #readline() method

f = open ("july15txtfile.txt", "r")
print(f.readline())




# return two lines
    # readline() method twice
    
f = open ("july15txtfile.txt", "r")
print(f.readline())
print(f.readline())




# Looping through files:
    # read the whole file, line by line:

f = open ("july15txtfile.txt", "r")
for x in f:
    print(x) ## adds extra lines

### OR ###
   
f = open ("july15txtfile.txt", "r")
for x in f:
    print(x, end ="") ## doesn't add extra lines in between




# CLOSE THE FILE WHEN DONE
    
f = open ("july15txtfile.txt", "r")
print(f.readline())
f.close()




#### Writing to an existing file:

# a - append
    # opens a file for appending
    # will append to the end of file
    # creates the file if it does not exist




# Open july15txtfile.txt and append content

f = open ("july15txtfile.txt", "a")
f.write("This is filler text because I am trying to add text to thsi file.")
f.close()
## nothing will happen in the Python shell, it will add to the txt file at the end!!!

# open and read file after appending:
f = open ("july15txtfile.txt", "r")
print(f.read())




### OVERWITE THE EXISTING CONTENT THE TEXT FILE
# w - write
    # will overwirte all the existing content

f = open ("july15txtfile.txt", "w")
f.write("Uh oh.... I think I deleted all of your text. Oops.")
f.close()

### then this opens and read the updated file:

f = open ("july15txtfile.txt", "r")
print(f.read())




## CREATE A NEW FILE USING PYTHON
    # use open() method, and on the following:
# x - create - will create a file, retuns an error if the file exist:

f = open("newtextJuly15.txt","x")


## a - append - will create the file if the specified file does not exist
## w - write - will create a file if the specified file does not exist


## r - read - if you attempt to read a file that does not exists then it will give you an error
## X - create - if you attempt to create a file that already exists, it will give you an error






## FILE DELETION

## os is an import package, allowing the python to your trash can to be able to rmeove it

# create the file first or it should already exist

# operating system = os

    ## import the os module
    ## run or.remove() function:

import os
os.remove("july15txtfile2.txt")





### if you want to prevenrt errors?
    # check if the file exists

import os
if os.path.exists("demofile.txt"):
    os.remove("domefile.txt")
    #then delete it!

else:
    print("The file does not exist.")





### REMOVE A FOLDER
    #** MUST BE IN THE SAME DIRECTORY

## first create the empty folder
    
import os
os.rmdir("testfolder")

## ONLY EMPTY FOLDERS CAN BE REMOVED! 







## No pratice this week!!

# in Python:
    # creata file called yourname.txt
f = open("hamida.txt","x")
    
    # add some text about yourself
    # save
    # add a fun fact about Aneesa
    # save
    # re-update the updated file





import os
# list all files in a directory using os.listdir

for entry un or.listdir(basepath):
    if os.path.isfile(
