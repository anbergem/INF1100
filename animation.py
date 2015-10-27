from matplotlib.pyplot import *
from numpy import *
import time

def f(x, t):
	return sin(x*0.01*t)/(x)

def g(x):
	return sin(x)/(x) +1 

x = linspace(-20,20,500)
s = zeros_like(x) # zeros with the same length as x


ion() #turn matplotlib interactive mode on
plot(x, g(x)) # plots the non-varying funktion g(x)

lines = plot(x,s) # plot x, s wich will result a line on y=0
				  # and save the plot to a variable

axis([-20, 20, -2, 6]) # lock the axis, since the frame in interactive

# make a list the varies from 0-250-0-250-0...
a = [i for i in range(0, 250, 5)]
a += reversed(a)
a += a
a += a

for t in a: 
    s = f(x,t) # set the whole s-array to f(x, t)
    		   # only one t-varlue, but all x-values
    lines[0].set_ydata(s) # set the y-component of the plot
    					  # to s-array
    draw()	# 'execute', plot this
    legend(['sin(x)/x', 't = %d' %t]) # varying legend
    time.sleep(0.00001) #wait 10us seconds per frames