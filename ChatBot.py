#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *


# In[2]:


root = Tk()


# In[3]:


root.title("Chat Bot")
root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)


# In[4]:


main_menu = Menu(root)


# In[5]:


# Create the submenu 
file_menu = Menu(root)

# Add commands to submenu
file_menu.add_command(label="New..")
file_menu.add_command(label="Save As..")
file_menu.add_command(label="Exit")
main_menu.add_cascade(label="File", menu=file_menu)
#Add the rest of the menu options to the main menu
main_menu.add_command(label="Edit")
main_menu.add_command(label="Quit")
root.config(menu=main_menu)


# In[6]:


chatWindow = Text(root, bd=1, bg="black",  width="50", height="8", font=("Arial", 18), foreground="#00ffff")
chatWindow.place(x=6,y=6, height=385, width=370)


# In[7]:


messageWindow = Text(root, bd=0, bg="black",width="30", height="4", font=("Arial", 18), foreground="#00ffff")
messageWindow.place(x=128, y=400, height=88, width=260)


# In[8]:


scrollbar = Scrollbar(root, command=chatWindow.yview, cursor="star")
scrollbar.place(x=375,y=5, height=385)


# In[9]:


Button= Button(root, text="Send",  width="12", height=5,
                    bd=0, bg="#0080ff", activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12))
Button.place(x=6, y=400, height=88)


# In[10]:


root.mainloop()


# In[ ]:





# In[ ]:




