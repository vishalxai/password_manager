from tkinter import *

window = Tk()

r= Label(bg="red",width= 20,height=5)
r.grid(row=0,column=0)

g=Label(bg="green",width=20,height=5)
g.grid(row=1,column=1)

b=Label(bg="blue",width=40, height=5)
b.grid(row=2,column=0,columnspan=2)
# 3 columns and 2 rows where label (0 column and row),new button(2 columnn and 0 row ) and button (1row and 1 and 2 column)
# entry = 2 row and 3rd column

window.mainloop()