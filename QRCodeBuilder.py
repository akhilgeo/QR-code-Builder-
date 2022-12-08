import tkinter as tk
from tkinter import ttk
from tkinter import * 
from PIL import ImageTk, Image
import qrcode
import os
import pyperclip

# this is a function to get the user input from the text input box
def getInputBoxValue():
    userInput = encodeText.get()
    return userInput

 
# this is the function called when the button is clicked
def btnClickFunction():
    encodeText = getInputBoxValue()
    img = qrcode.make(encodeText)
    img.show()
    img = img.save('QRCODEBUILDER.png')
    

root = Tk()

# This is the section of code which creates the main window
root.geometry('515x226')
root.configure(background='#F0F8FF')
root.title('QR Code Builder - AKHILGEORGE.COM')

# This is the section of code which creates a text input box
encodeText=Entry(root)
encodeText.place(x=250, y=119)
#Logo
img = ImageTk.PhotoImage(Image.open( os.path.dirname(os.path.realpath(__file__))+"\img\logo.png"))
panel = tk.Label(root, image = img, width=120, height=60, bg='#F0F8FF')
panel.place(x=51, y=30)
panel.pack(side = "top", fill = "both")

# This is the section of code which creates the a label
Label(root, text='Text to Encode', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=119, y=117)

# This is the section of code which creates a button
Button(root, text='Build QR Code', bg='#E0EEEE', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=230, y=158)

root.mainloop()
