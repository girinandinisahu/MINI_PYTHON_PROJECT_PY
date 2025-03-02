import random
import tkinter as tk
from tkinter import messagebox

def play_game(user_choice):
    computer = random.choice([-1, 0, 1])
    youDict = {"s": 1, "w": -1, "g": 0}
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
    you = youDict[user_choice]

    result_message = f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}\n"
    ''''
    if(computer == -1 and you == 1): (Computer - you ) = -2
        print("You Win!")
    elif(computer == -1 and you == 0):   (Computer - you ) = -1
        print("You Lose!")
        
    if(computer == 1 and you == -1):   (Computer - you ) = 2
        print("You Lose!")
    elif(computer == 1 and you == 0):   (Computer - you ) = 1
        print("You Win!")
    
    if(computer == 0 and you == -1):   (Computer - you ) = 1
        print("You Win!")
    elif(computer == 0 and you == 1):   (Computer - you ) = -1
        print("You Lose!")
        
    else:
        print("Somethings went wrong")
        
        
 Below logic is written on the basices of (compurt - you ) value
        '''
    if computer == you:
        result_message += "It is a draw"
    elif (computer - you) == -1 or (computer - you) == 2:
        result_message += "You Lose!"
    else:
        result_message += "You Win!"

    messagebox.showinfo("Game Result", result_message)

def on_button_click(choice):
    # Change button color for animation effect
    btn_snake.config(bg="lightblue")
    btn_water.config(bg="lightblue")
    btn_gun.config(bg="lightblue")
    
    play_game(choice)
    
    # Reset button colors after a short delay
    root.after(200, reset_button_colors)

def reset_button_colors():
    btn_snake.config(bg="SystemButtonFace")
    btn_water.config(bg="SystemButtonFace")
    btn_gun.config(bg="SystemButtonFace")

# Create the main window
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("400x300")  
root.iconbitmap("icon.ico")  

icon_snake = tk.PhotoImage(file="snake_icon.png")  
icon_water = tk.PhotoImage(file="water_icon.png") 
icon_gun = tk.PhotoImage(file="gun_icon.png")     

btn_snake = tk.Button(root, text="Snake (s)", image=icon_snake, compound=tk.LEFT, command=lambda: on_button_click("s"), width=100, height=50)
btn_water = tk.Button(root, text="Water (w)", image=icon_water, compound=tk.LEFT, command=lambda: on_button_click("w"), width=100, height=50)
btn_gun = tk.Button(root, text="Gun (g)", image=icon_gun, compound=tk.LEFT, command=lambda: on_button_click("g"), width=100, height=50)

btn_snake.pack(pady=10,)
btn_water.pack(pady=10)
btn_gun.pack(pady=10)

# Start the GUI event loop
root.mainloop()