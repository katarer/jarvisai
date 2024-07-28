from tkinter import *  # pip install tkinter
from PIL import Image, ImageTk, ImageSequence  # pip install Pillow
import time
import pygame  # pip install pygame
from pygame import mixer

mixer.init()

root = Tk()
root.geometry("1000x500")


def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    root.configure(background='black')
    global img
    img = Image.open("iron.gif")
    lbl=Label(root)
    lbl.place(x=0, y=0)
    i = 0
    mixer.music.load("finger.mp3")
    mixer.music.play()

    for img in ImageSequence.Iterator(img):
        img = img.resize((1000, 500))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.05)
    root.destroy()

play_gif()
root.mainloop()

# from tkinter import *
# from PIL import Image, ImageTk, ImageSequence
# import pygame
# from pygame import mixer
# import os
#
# # Initialize Pygame mixer for playing music
# mixer.init()
#
# # Create a Tkinter root window
# root = Tk()
# root.attributes("-fullscreen", True)  # Make the window fullscreen
# root.configure(background='black')  # Set background color to black
#
# # Get the screen width and height
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()


# def play_gif():
#     root.lift()
#     root.attributes("-topmost", True)
#     global img_label
#     img = Image.open("iron.gif")
#     img = img.resize((screen_width, screen_height))  # Resize the image to fit the screen
#     img = ImageTk.PhotoImage(img)
#     img_label = Label(root, image=img, bg="black")
#     img_label.place(x=0, y=0)
#
#     # Load and play the background music using Pygame mixer
#     mixer.music.load("music.mp3")
#     mixer.music.play()
#
#     for img in ImageSequence.Iterator(img):
#         img = img.resize((screen_width, screen_height))  # Resize each frame to fit the screen
#         img = ImageTk.PhotoImage(img)
#         img_label.config(image=img)
#         root.update()
#
#     root.destroy()
#
#
# play_gif()
# root.mainloop()


from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import pygame
from pygame import mixer
import os

# Initialize Pygame mixer for playing music
mixer.init()

# Create a Tkinter root window
root = Tk()
root.attributes("-fullscreen", True)  # Make the window fullscreen
root.configure(background='black')  # Set background color to black

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


# def play_gif():
#     root.lift()
#     root.attributes("-topmost", True)
#     global img_label
#
#     # Open the GIF image
#     img = Image.open("iron.gif")
#     img = img.resize((screen_width, screen_height))  # Resize the image to fit the screen
#     img = ImageTk.PhotoImage(img)
#
#     # Create a label to display the GIF animation
#     img_label = Label(root, bg="black")
#     img_label.place(x=0, y=0)
#
#     # Load and play the background music using Pygame mixer
#     mixer.music.load("music.mp3")
#     mixer.music.play()
#
#     # Iterate over the frames of the GIF and display each frame
#     for frame in ImageSequence.Iterator(img):
#         frame = frame.resize((screen_width, screen_height))  # Resize each frame to fit the screen
#         frame = ImageTk.PhotoImage(frame)
#         img_label.config(image=frame)
#         root.update()
#
#     root.destroy()
#
#
# play_gif()
# root.mainloop()
