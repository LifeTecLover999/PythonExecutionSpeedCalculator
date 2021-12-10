from tkinter import *
import time
root = Tk()
root.title('PESC')
lab = Label(root)
lab.pack()
root.geometry("1080x720")

def update():
   t_end = time.time() + 1
   i = 0
   while time.time() < t_end:
      i = i + 1
   iString = str(i)
   lab['text'] = iString + " lines of code/second"
   root.after(1000, update) # run itself again after 1000 ms

update()

root.mainloop()