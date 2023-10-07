#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import pandas as pd


# In[2]:


df = pd.read_excel(r'C:\Users\sarah\Downloads\Sample_Composition_Data.xls')
df


# In[3]:


# Create object 
root = Tk()

# Adjust size 
root.geometry( "600x600" )

# Change the label text 
def show(): 
    label.config( text = clicked.get() )
    
#column names

namesRocks = df.to_numpy()[:, 0]
namesRocks = namesRocks[:]
namesRocks = namesRocks.tolist()
    
    # Dropdown menu options 
options = namesRocks
 
# datatype of menu text 
clicked = StringVar() 
  
# initial menu text 
clicked.set( "Select Your Rock" ) 
  
# Create Dropdown menu 
drop = OptionMenu( root , clicked , *options ) 
drop.pack() 
  
# Create button, it will change label text 
button = Button( root , text = "click Me" , command = show ).pack() 
  
# Create Label 
label = Label( root , text = " " ) 
label.pack() 
  
# Execute tkinter 
root.mainloop() 


# In[ ]:


for i in range shape{
   df.loc[i,"Std name"] 
}


# In[ ]:


cols= df.columns
cols


# In[ ]:


#column names
namesRocks = df.to_numpy()[:, 0]
namesRocks = namesRocks[:]
namesRocks = namesRocks.tolist()


# In[ ]:





# In[ ]:




