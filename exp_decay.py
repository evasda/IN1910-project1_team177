from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

class ExponentialDecay:
	"""Class for solving ODE of the form du/dt = -a*u."""
	def __init__(self, a):
		self.a = a

	def __call__(self, t, u):
		"""Returns the derivative of u."""
		a = self.a
		derivative = -a*u
		derivative = np.round(derivative, 7)
		return derivative

	def solve(self, u0, T, dt):
		"""Method takes in the derivative, initial value, end of interval and size of increment. Returns t values and y values as arrays."""
		sol = solve_ivp(self.__call__, [0,T], u0, t_eval = list(np.linspace(0, T, T/dt)))
		return sol.t, sol.y[0]

if __name__ == "__main__":
    """Example for a given set of values, and the resulting plot"""
    a=0.8
    u0 = [10]
    T = 10
    dt = 0.1
    decay_model = ExponentialDecay(a)
    t, u = decay_model.solve(u0, T, dt)
    plt.plot(t, u)
    plt.show()

