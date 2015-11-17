from ODESolver import ForwardEuler, RungeKutta4
import numpy as np
import matplotlib.pyplot as plt

class Current:
	def __init__(self, E, R, L):
		self.E, self.R, self.L = E, R, L

	def __call__(self, i, t):
		E, R, L = self.E, self.R, float(self.L)
		return (E-R*i)/L

class Exact(Current):
	def __call__(self, t):
		E, R, L = self.E, self.R, float(self.L)
		return (float(E)/R)*(1-np.exp(-(R*t)/L)) 

def _demo():
	R = 175 # Ohm
	L = 69e-3 # Henry
	E = 6.3   # Volt
	
	for i in 5, 10, 50:
		didt = Current(E, R, L)
		t_points = np.linspace(0, 2e-3, i)

		i0 = 0
		for solver_class in ForwardEuler, RungeKutta4:
			solver = solver_class(didt)
			solver.set_initial_condition(i0)
			u, t = solver.solve(t_points)
			plt.plot(t, u, label=solver_class.__name__)
		
		I = Exact(E, R, L)
		plt.plot(t, I(t), '--', label='exact')
		plt.legend(loc='best')
		plt.xlabel('t [s]')
		plt.ylabel('I(t) [A]')
		plt.title('RL-Circuit')
		plt.show()



if __name__ == '__main__':
	_demo()
