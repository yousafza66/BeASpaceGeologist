#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import pandas as pd
from PIL import Image,ImageTk


# In[2]:


df = pd.read_excel(r'C:\Users\sarah\Downloads\Sample_Composition_Data.xls')
df


# In[ ]:


#Create an instance of tkinter frame
root = Tk()

# Adjust size 
root.geometry( "800x800" )

#Load an image in the script
img= (Image.open("rockstar.jpg"))

#Resize the Image using resize method
resized_image= img.resize((314,185), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

# Change the label text and image
def show(): 
    label.config( text = clicked.get() ) #text is the name of the image we want
    
    img2=(Image.open(clicked.get() + ".jpg"))
    
    resized_rocks= img2.resize((200,200), Image.ANTIALIAS)
    new_rocks= ImageTk.PhotoImage(resized_rocks)
    
    label.configure(image=new_rocks)
    label.image=new_rocks    
    
#column names
namesRocks = df.to_numpy()[:, 0]
namesRocks = namesRocks[:]
namesRocks = namesRocks.tolist()
    
# Dropdown menu options 
options = namesRocks
#root['background'] = 'blue'
 
# datatype of menu text 
clicked = StringVar() 
  
# initial menu text 
clicked.set( "Select Your Rock" ) 
  
# Create Dropdown menu 
drop = OptionMenu( root , clicked , *options ) 
drop.pack() 
  
# Create button, it will change label text  and change image
button = Button( root , text = "Enter" , command = show ).pack() 

# Create Label for rock name
label = Label( root , text = " " ) 
label.pack() 

# Create a label to display the image
label= Label(root,image= new_image)
label.pack()

# Execute tkinter
root.bind("<Return>", show)
root.mainloop() 


# In[ ]:





# In[ ]:


cols= df.columns
cols


# In[ ]:


#column names
namesRocks = df.to_numpy()[:, 0]
namesRocks = namesRocks[:]
namesRocks = namesRocks.tolist()


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



root.mainloop()


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





# In[ ]:




