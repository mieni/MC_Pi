import random #used for generation of numbers
import threading # used to make a threading
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import sys #import Tkinter
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
    from tkinter import messagebox

root = Tk.Tk() #create object
root.wm_title("MC calculation of Pi") #title
menu = Tk.Menu(root) # create Menu
root.config(menu=menu)

def openFrame(): #create About window
    AboutFrame = Tk.Toplevel()
    AboutFrame.geometry("400x300")
    AboutFrame.title("About")
    T = Tk.Text(AboutFrame, )
    T.pack()

    info =  """
A simple program for Monte Carlo calculation of Pi. The program shows the convergence of the obtained value with the number of generated numbers.

Developed by Mieni
"""
    T.insert(Tk.END, info)
    T['state']='disabled' # disable the editing

helpmenu = Tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...",command=openFrame)

#create frames and their geometry( I used more columns than necessary)
toolframe=Tk.Frame(root)
toolframe.grid(row=0,columnspan=4,sticky=Tk.W)
upframe=Tk.Frame(root)
upframe.grid(row=1,columnspan=4)
buttonframe=Tk.Frame(root)
buttonframe.grid(row=2,columnspan=4)

#create the plot figure
figure_plot = Figure()
plot = figure_plot.add_subplot(111)
plot.grid()
plot.set_title("Pi")
plot.set_xlabel("# of generated numbers")
plot.set_ylabel("Value of Pi")
plot.axhline(y=3.14159265359)

#add it to the frame
canvas = FigureCanvasTkAgg(figure_plot, master=upframe)
canvas.show()
canvas.get_tk_widget().grid(columnspan=4)

toolbar = NavigationToolbar2TkAgg(canvas, toolframe)
toolbar.update()
canvas._tkcanvas.grid(columnspan=4)

#create a diferent thred in order for the program not to halt while generating random numbers
def call_plot():
    thred=threading.Thread(target=_cal)
    thred.start()
#draw the plot
def _cal():
    plot.clear()
    gen_dots=int(entry_field.get()) #get the max_iteration from entry field

#see how many dots are going to be generated to see wether to draw the first 10, where the deviation from Pi is segnificant
    if gen_dots <=100:
        d_marg=1
    else:
        d_marg=10

    xdata = []
    ydata = []
    t = []
    for nit in range(10,gen_dots):
       count=0
       for num in range(1,nit):
          x= random.random()
          y= random.random()
          d=x*x+y*y
          if d < 1.0 :
             count=count+1
       t.append(count)
       t[-1]=count*4/nit
       xdata.append(nit)
       ydata.append(t[-1])
#plot the data
    plot.set_autoscaley_on(True)
    plot.grid()
    plot.set_title("Pi")
    plot.set_xlabel("# of generated numbers")
    plot.set_ylabel("Value of Pi")
    plot.axhline(y=3.14159265359)


    plot.plot(xdata,ydata, 'ro',ms=1)
    canvas.draw()

#button for the plotting
Plot_btn = Tk.Button(master=buttonframe, text='Plot', command=call_plot)
Plot_btn.grid(row=1,column=5)

#entry field to get the max # of generated numbers
Tk.Label(buttonframe,text='Max # of generated numbers').grid(row=1,column=0,)
entry_field=Tk.Entry(buttonframe,width=5)
entry_field.insert(0,"1000")
entry_field.grid(row=1,column=1,sticky=Tk.W)

Tk.mainloop()
