# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 23:02:42 2024

@author: hiraa
"""

def happy_birthday(name,age):
    print(f"happy birthday to {name}")
    print(f"you are year {age} now")
    print("are you happy?")
    
happy_birthday("bro",78)

happy_birthday("pizza",67)

happy_birthday("catto",20)

def intro(name,cclas,person,hair,shoes):
    print(f"hi! im {name}")
    print(f"im in same class as yours . class {cclas}")
    print(f"it was nice meeting {person}. you have amazing {hair} and i like your {shoes}")

intro("raven", "cys66", "sam", "blck hair", "red shoes")
intro("google", "weber", "sam", "personality", "bag")

import tkinter as tk

window = tk.Tk()
window.title = ("my app")
window.config(bg = "red")
window.geometry("300x500")

window.mainloop()