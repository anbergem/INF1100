from matplotlib.pyplot import plot, show, axis, title,\
							  legend, xlabel, ylabeln
from numpy import linspace, cos, sin, pi

def f(t):
	return sin(t)/t

def g(t):
	return sin(2*t)/t + 1

t = linspace(-50, 50, 1000)

plot(t, f(t), 'go')
plot(t, g(t))

title('t = sin xt/t')
legend(['sin t/t', 'sin(2t)/t + 1'])
xlabel('t')
ylabel('f(t)')


show()