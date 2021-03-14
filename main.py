import tkinter as tk 
import math
import winsound
import csv 
import random
import threading
from PIL import Image, ImageTk

# def createNewWindow():
#   newWindow = tk.Toplevel(app)
s =""

def show_result(): 
  outcome = choose()
  food_label['text'] = '{} '.format(outcome)
  food_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

def choose(): 
  #  random choose 
  data = open('foood.csv' ,newline="")
  reader = csv.reader(data)
  count= len(list(reader))
  random_n = random.randint(1,count)
  data.seek(0) # to handle repeat reading problem 
  for i, row in enumerate(reader):   
    if i+1 ==  random_n:
      outcome = s.join(row) 
  return outcome         


root = tk.Tk()
# root.attributes('-fullscreen', True)
root.resizable(width=False, height=False)
root.title("食")
root.geometry('1078x578') 
# background
bg = tk.PhotoImage(file = "back1.png") 
# Show image using label 
label1 = tk.Label( root, image = bg) 
label1.place(x = 0, y = 0) 
food_label = tk.Label(root, font=('標楷體', 35), fg='MidnightBlue')
tk.Button(text='我想來點....', font=('微軟正黑體', 25),command=show_result).place(relx=0.9, rely=0.9, anchor=tk.CENTER)
root.mainloop()