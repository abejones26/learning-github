# Create a variable and set it as an List
import random
myList = ["Jacob", 25, "John", 80]
# print(myList)

# Adds an element onto the end of a List
myList.append("Matt")
print(myList)

# Returns the index of the first object with a matching value
print(myList.index("Matt"))

# Changes a specified element within an List at the given index
# ['Jacob', 25, 'John', 80, 'Matt']
# [1,2,3,4,5] # Value counts
# [0,1,2,3,4] # Offset of a value count - this is how the computer read lines

myList[3] = 85
print(myList)

# Returns the length of the List
print(len(myList))

# Removes a specified object from an List
myList.remove("Matt")
print(myList)

# Removes the object at the index specified
myList.pop(0)  # [25, 'John', 85]
myList.pop(0)  # ['John', 85]
myList.pop(0)  # [85]
print(myList)

# Creates a tuple, a sequence of immutable Python objects that cannot be changed
myTuple = ('Python', 100, 'VBA', False)
print(myTuple)

# Student Activity start here
print("This is our random number: " + str(random.randint(0, 9)))

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = []

# Computer Selection
computer_choice = random.choice()

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if (user_choice == "r" and computer_choice == "p"):
    print("You chose rock. The computer chose paper.")
    print("Sorry. You lose.")

elif (user_choice == "r" and computer_choice == "s"):
    print("You chose rock. The computer chose scissors.")
    print("Yay! You won.")

elif (user_choice == "r" and computer_choice == "r"):
    print("You chose rock. The computer chose rock.")
    print("A smashing tie!")

elif (user_choice == "p" and computer_choice == "p"):
    print("You chose paper. The computer chose paper.")
    print("A smashing tie!")

# elif (user_choice == "p" and computer_choice == "s"):
#     # print("You chose paper. The computer chose scissors.")
#     # print("Sorry. You lose.")

# elif (user_choice == "p" and computer_choice == "r"):
#     # print("You chose paper. The computer chose rock.")
#     # print("Yay! You won.")

# elif (user_choice == "s" and computer_choice == "p"):
#     # print("You chose scissors. The computer chose paper.")
#     # print("Yay! You won.")

# elif (user_choice == "s" and computer_choice == "s"):
#     # print("You chose scissors. The computer chose scissors.")
#     # print("A smashing tie!")

# elif (user_choice == "s" and computer_choice == "r"):
#     # print("You chose scissors. The computer chose rock.")
#     # print("Sorry. You lose.")

# else:
#     # print("I don't understand that!")
#     # print("Next time, choose from 'r', 'p', or 's'.")
