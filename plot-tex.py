from matplotlib.pyplot import plot, show, axis, title,\
							  legend, xlabel, ylabel, rc
from numpy import linspace, cos, sin, pi

#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:

#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

def f(t):
	return sin(t)/t

def g(t):
	return sin(2*t)/t + 1

r = 5
t = linspace(-50, 50, 1000)

plot(t, f(t), 'go')
plot(t, g(t))

title(r'$ f(t) = \frac{\sin t}{t}$')
legend([r'$\frac{\sin t}{t}$', r'$\frac{\sin 2t}{t}+1$'])
xlabel(r'$t$')
ylabel(r'$f(t)$')


show()