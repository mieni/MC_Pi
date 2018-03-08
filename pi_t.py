import matplotlib.pyplot as plt #used for ploting
import random #used for generation of numbers

def draw(gen_dots):

#see how many dots are going to be generated to see wether to draw the first 10, where the deviation from Pi is segnificant
    if gen_dots <=100:
        d_marg=1
    else:
        d_marg=10

    xdata = []
    ydata = []
    t = []

    for nit in range(d_marg,gen_dots):
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
    plt.autoscale(True)
    plt.grid()
    plt.title("Pi")
    plt.xlabel("# of generated numbers")
    plt.ylabel("Value of Pi")
    plt.axhline(y=3.14159265359)
    plt.plot(xdata,ydata, 'ro',ms=1)
    plt.show()

# a simple menu for the program
info =  """
A simple program for Monte Carlo calculation of Pi. The program shows the convergence of the obtained value with the number of generated numbers.

Developed by Mieni

"""
print(info)
#main loop
while 1:
    inp = input("Enter <exit> to exit \nEnter the number of generated numbers: ")
    print('\n')
    if inp == 'exit':
        break #exit if exit
    else:
        try:
            int(inp) #exception
            draw(int(inp)) #plot
        except ValueError:
            #Handle the exception
            print ('Please enter an integer')
