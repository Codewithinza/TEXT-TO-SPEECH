import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox

import pyttsx3
import os

engine = pyttsx3.init()

def speak():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty("voices")
    
    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
            setvoice()
        elif speed == "Normal":
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()
   
def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty("voices")
    
    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'thespeech.mp4')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'thespeech.mp4')
            engine.runAndWait()
 
    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
            setvoice()
        elif speed == "Normal":
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()

def clearText():
    text_area.delete(1.0, END)

def Close(): 
    root.destroy() 

root = Tk()
root.title("Text to Speech")
root.geometry("900x450+300+200")
root.resizable(False, False)
root.configure(bg="#F5CBA7")  # baby pink background

# icon
image_icon = PhotoImage(file="image/speak_speech.png")
root.iconphoto(False, image_icon)

# ----- Top Frame -----
Top_frame = Frame(root, bg="#EBDEF0", width=900, height=100)  # sky blue background
Top_frame.place(x=0, y=0)

Logo = PhotoImage(file="image/speaker.png")
Label(Top_frame, image=Logo, bg="#EBDEF0").place(x=10, y=5)

Label(Top_frame, text="TEXT TO SPEECH", font="arial 20 bold", bg="#EAFAF1", fg="black").place(x=120, y=30)

# ----- Main View -----

text_area = Text(root, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

Label(root, text="VOICE", font="arial 18 bold", bg="#FCE4EC", fg="#F06292").place(x=580, y=130)
Label(root, text="SPEED", font="arial 18 bold", bg="#305065", fg="white").place(x=760, y=130)

gender_combobox = Combobox(root, values=['Male', 'Female'], font="arial 14", state='readonly', width=10)
gender_combobox.place(x=550, y=175)
gender_combobox.set('Male')

speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state='readonly', width=10)
speed_combobox.place(x=730, y=175)
speed_combobox.set('Normal')

imageIcon1 = PhotoImage(file="image/speak55.png")
btn_speak = Button(root, text=" Speak", compound=LEFT, image=imageIcon1, width=130, font="arial 14 bold", command=speak)
btn_speak.place(x=550, y=250)

imageIcon2 = PhotoImage(file="image/download55.png")
btn_save = Button(root, text=" Save", compound=LEFT, image=imageIcon2, width=130, bg="#808000", font="arial 14 bold", command=download)
btn_save.place(x=730, y=250)

clear_button = Button(root, text="Clear Text", font="arial 18 bold", command=clearText)
clear_button.place(x=550, y=350)

# Button for closing
exit_button = Button( bg="yellow", fg="black",text="Exit", font="arial 18 bold", width=8, command=Close)
exit_button.place(x=735, y=350)

root.mainloop()
