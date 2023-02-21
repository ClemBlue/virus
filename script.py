import tkinter as tk
import random
import os
import time

username = os.getlogin()

creepyText = [
    "Watching you",
    "No way out",
    "Don't open the door",
    "You are not alone",
    "It's comming",
    "You are playing my game now",
    "Getting closer",
    "Don't move",
    "Hurry",
    "It's comming for you " + username
]

def randomNumber(min, max):
    randomNB = random.randint(min, max)
    return randomNB

def popUps():
    root = tk.Tk()
    root.configure(background="black")

    #To disable the menu
    root.overrideredirect(True)

    nb = randomNumber(0, 9)
    #root.title('Creepy')

    label = tk.Label(root, text=creepyText[nb], bg='black', fg='white')
    root.geometry('300x100')

    label.pack()
    root.after(1000, root.destroy)
    root.mainloop()

start_time = time.time()
interval = 1
for i in range(20):
    time.sleep(start_time + i*interval - time.time())
    popUps()
