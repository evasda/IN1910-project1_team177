import scipy
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

class ExponentialDecay:
	def __init__(self, a):
		self.a = a

	def __call__(self, t, u):
		a = self.a
		derivative = -a*u
		return derivative

	def solve(self, u0, T, dt):
		sol = solve_ivp(self.__call__, [0,T], u0, t_eval = list(np.linspace(0, T, T/dt)))
		return sol.t, sol.y[0]


ED = ExponentialDecay(0.4)
deriv = ED(1, 3.2)
print(deriv)

a=0.4
u0 = [3]
T = 10
dt = 0.1

decay_model = ExponentialDecay(a)
t, u = decay_model.solve(u0, T, dt)
print(t,u)

plt.plot(t, u)
plt.show()



"""
Now, extend your class with a method solve(u0, T, dt) that solves the ODE for a given initial condition $u_0$ on the interval $t \in (0, T]$ in steps of $\Delta t$. The method should return two arrays, one for the time points and one for the solution points $u(t_i)$.

Hint 1: The initial condition that is sent into solve_ivp has to be a sequence (in case of several ODEs), and so you will need to send it in as a tuple (u0,) 
or a list [u0].
Hint 2: To enforce a specific time discretization $\Delta t$, you need to use the t_eval keyword argument.
If implemented correctly, the class should be able to be used as follows.
"""