from Tkinter import *
from tkFileDialog import askopenfilename
import Tkinter
import tkFileDialog
"""
file = Tkinter.Tk()
file.withdraw()
filename = tkFileDialog.askopenfilename(parent=file)

master = Tk()
master.title("Choose a filter")
master.geometry ("300x150")

text = Text(master,height = 3)
text.insert(INSERT,"Please Select a Filter")
text.pack()

bottom = Frame(master)
bottom.pack(side = BOTTOM)

var = StringVar(master)
var.set("Purple") # initial value

option = OptionMenu(bottom, var, "Purple", "Green", "Blend", "Binary")
option.pack(side = LEFT)

def ok():
    print "value is", var.get()
    master.quit()

button = Button(bottom, text="OK", command=ok)
button.pack(side = RIGHT)

master.mainloop()"""

'''
root = Tk()
photo = PhotoImage(file = 'testmanipulation.png')# only works with png images....

label = Label(root, image = photo)
label.pack()

root.mainloop()
'''
#from practice import *

#from coleman import *

'''
file = Tkinter.Tk()
file.withdraw()
filename = tkFileDialog.askopenfilename(parent=file)
# This is where I will bring the place as to where the user will set the image.
print(filename)
'''


master = Tk()
master.title("Choose a filter")
master.geometry ("400x250")

topFrame = Frame(master)
topFrame.pack()

button1 = Button(topFrame, text = "Red", fg = "red", command = filterAlgorithm1)

button2 = Button(topFrame, text = "Blue", fg = "blue", command = printhi)
button3 = Button(topFrame, text = "Green", fg = "green", command = printhi)
button4 = Button(topFrame, text = "Blend", fg = "purple", command = printhi)
quit = Button(topFrame, text = "Quit", fg = "black", command = topFrame.quit)



button1.grid(row = 0, sticky = E)
button2.grid(row = 1, sticky = E)
button3.grid(row= 2, sticky = E)
button4.grid(row = 3, sticky = E)
quit.grid( row = 4, sticky = E)
master.mainloop()



'''

button1.pack(side = RIGHT)
button2.pack(side = RIGHT)
button3.pack(side = RIGHT)
button4.pack(side = BOTTOM)
quit.pack(side = RIGHT)
'''







































master.mainloop()
