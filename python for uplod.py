#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the necessary module
import tkinter

# Function for the Heads and Tails game
def heads_and_tails():
    print ("Welcome to Heads and Tails game")
    user_input = input("Heads or Tails: ")
    valid_input = ["heads", "tails"]
    print("You chose", user_input)
    
    # Checking if the user input is valid
    if user_input not in valid_input:
        print("please enter valid input")
    else:
        print("let's toss the coin")
        import random
        
        # Simulating the coin toss
        if random.choice("ht") == "h":
            coin_result = "heads"
        else:
            coin_result = "tails"
        
        print("Coin Result is", coin_result)
        
        # Determining the winner
        if user_input == coin_result:
            print("You Win")
        else:
            print("You Lose")

# Function for the Dice game
def dice():
    import random
    print("Welcome to dice ")
    user_input = int(input("Guess the number: "))
    dice_result = random.randrange(1, 7)
    valid_input = [1, 2, 3, 4, 5, 6]
    
    # Checking if the user input is valid
    if user_input not in valid_input:
        print("Please enter valid number")
    else:
        # Determining the winner
        if user_input == dice_result:
            print("Dice result is", dice_result)
            print("You Win")
        else:
            print("Dice result is", dice_result)
            print("You lose")

# Function for the Cubes game
def cubes():
    print("Welcome to cubes")
    user = int(input("Enter your number: "))
    
    # Displaying the cubes of numbers in reverse order
    for i in range(user, 0, -1):
        cube = i * i * i
        print("Cube of", i, "is", cube)

# Creating the main window using tkinter
window = tkinter.Tk()

# Setting the window dimensions
window.geometry("500x500")

# Setting the window title
window.title("python project - Raj")

# Creating labels and buttons using tkinter
lab = tkinter.Label(window, text='PYTHON PROJECT', font=("Arabic", 18))
lab.place(x=135, y=35)

lab1 = tkinter.Label(window, text='Made by Raj', font=("Arabic", 14))
lab1.place(x=185, y=70)

key = tkinter.Button(window, text="heads_and_tails", height=3, width=18, command=heads_and_tails)
key.place(x=190, y=120)

key2 = tkinter.Button(window, text="dice", height=3, width=18, command=dice)
key2.place(x=190, y=200)

key3 = tkinter.Button(window, text="cubes", height=3, width=18, command=cubes)
key3.place(x=190, y=280)

# Running the main loop of the tkinter window
window.mainloop()


# In[ ]:




