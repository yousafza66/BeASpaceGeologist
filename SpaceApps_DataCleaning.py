#!/usr/bin/env python
# coding: utf-8

# Note: Need to run the 'pip 'cmd below once!

# In[ ]:


get_ipython().system('pip install ttkbootstrap ')


# In[1]:


from tkinter import *
import pandas as pd
from PIL import Image,ImageTk

# Modifications to GUI interface
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


# In[2]:


df = pd.read_excel(r'C:\Users\sarah\Downloads\Sample_Composition_Data.xls')


# In[ ]:


# Create an instance of tkinter frame
root = ttk.Window(themename = "yeti")

# Adjust size 
root.geometry( "800x800" )

# Load an image in the script
img= (Image.open("rockstar.png"))

# Resize the image using resize method
resized_image= img.resize((714,485), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

# Change the label text and image
def show(): 
    label.configure( text = clicked.get(), font = ("Arial", 20))
    
    img2=(Image.open("rocks/" + clicked.get() + ".jpg"))
    resized_rocks= img2.resize((200,200), Image.ANTIALIAS)
    new_rocks= ImageTk.PhotoImage(resized_rocks)
    
    label_image.configure(image=new_rocks)
    label_image.image=new_rocks    
    
#column names
namesRocks = df.to_numpy()[:, 0]
namesRocks = namesRocks[:]
namesRocks = namesRocks.tolist()
    
# Dropdown menu options 
options = namesRocks
 
# datatype of menu text 
clicked = StringVar() 
  
# initial menu text 
clicked.set( "Select Your Rock") 
  
# Create Dropdown menu 
drop = OptionMenu( root , clicked , *options ) 
drop.pack() 
  
# Create button, it will change label text  and change image
button = Button( root , text = "Enter", font = ("Arial", 10), command = show ).pack() 

# Create Label for rock name
label = Label( root , text = " ", font = ("Arial", 20)) 
label.pack() 

# Create a label to display the image
label_image = Label(root,image= new_image)
label_image.pack()

# Execute tkinter
root.bind("<Return>", show)
root.mainloop() 


# In[ ]:





# EXTRAS BELOW

# In[ ]:


# Import required libraries
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry("700x500")

frame = Frame(win, width=50, height=50)
frame = img.resize((50, 50), Image.ANTIALIAS) #
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("forest.jpg"))
win.mainloop()


# In[ ]:


#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk

#Create an instance of tkinter frame
win = Tk()

#Set the geometry of tkinter frame
win.geometry("750x270")

#Create a canvas
canvas= Canvas(win, width= 600, height= 400)
canvas.pack()

#Load an image in the script
img= (Image.open("forest.jpg"))

#Resize the Image using resize method
resized_image= img.resize((300,205), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(20,20, anchor=NW, image=new_image)

win.mainloop()


# In[ ]:


from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename = "superhero")

root.title("TTK Bootstrap")

my_label = tb.Label(text = "Hello World!" , font = ("Helvetica" , 20), bootstyle = "default" )
my_label.pack(pady = 50)
root.geometry('500x350')

root.mainloop()


# In[ ]:





# In[ ]:




