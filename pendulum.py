from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

class Pendulum:
	def __init__(self, g = 9.81 , L = 1., M = 1.):
		"""g is gravity, L is length of pendulum, M is mass of pendulum. """
		self.g = g
		self.L = L
		self.M = M

	def __call__(self, t, y):
		""" Returns derivatives as tuple of theta and omega values."""
		g = self.g
		L = self.L
		deriv_omega = -(g/L)*np.sin(y[0])
		deriv_theta = y[1]
		return [deriv_theta, deriv_omega]

	def solve(self, y0, T, dt, angles):
		"""
		Method takes in the derivative, initial value, end of interval and size of increment. 
		Last arguments specifies if the angle is given in degrees or radians.
		Returns the solution to the differential equation, returns omega, theta and t as arrays.
		"""
		if angles == "deg":
			y0[0] = y0[0]* np.pi/180.
			y0[1] = y0[1]*np.pi/180.
		sol = solve_ivp(self.__call__, [0,T], y0, t_eval = list(np.linspace(0, T, T/dt)))
		self._omega = sol.y[1]; self._theta = sol.y[0]
		self._t = sol.t

	@property
	def t(self):
		""" Returns array of t's."""
		try:
			return self._t
		except AttributeError:
			print("Must use method solve first.")
			raise

	@property
	def theta(self):
		""" Returns array of thetas."""
		try:
			return self._theta
		except AttributeError:
			print("Must use method solve first.")
			raise

	@property 
	def omega(self):
		""" Returns array of omegas."""
		try:
			return self._omega
		except AttributeError:
			print("Must use method solve first.")
			raise

	@property 
	def x(self):
		""" Returns array of x's."""
		self._x = self.L * np.sin(self._theta)
		return self._x

	@property
	def y(self):
		""" Returns array of y's."""
		self._y = -self.L * np.cos(self._theta)
		return self._y


	@property
	def potential(self):
		""" Returns potential energy as array."""
		self._potential = self.M*self.g*(self.y+self.L)
		return self._potential

	@property 
	def vx(self):
		""" Returns velocity vx as an array."""
		self._vx = np.gradient(self.x, self.t)
		return self._vx

	@property 
	def vy(self):
		""" Returns velocity vy as an array."""
		self._vy = np.gradient(self.y, self.t)
		return self._vy

	@property 
	def kinetic(self):
		""" Returns kinetic energy as an array."""
		self._K = 1./2 * self.M * (np.square(self.vx) + np.square(self.vy))
		return self._K


class DampenedPendulum(Pendulum):
	def __init__(self, g = 9.81 , L = 1., M = 1., B=1.):
		"""Extends class Pendulum with dampening parameter B. """
		self.g = g
		self.L = L
		self.M = M
		self.B = B

	def __call__(self, t, y):
		"""Returns theta and omega as a tuple."""
		g = self.g
		L = self.L
		B = self.B
		M = self.M
		deriv_omega = -(g/L)*np.sin(y[0]) - (B/M)*y[1]
		deriv_theta = y[1]
		return [deriv_theta, deriv_omega]





if __name__ == "__main__":
	y0 = [np.pi/4., 0.1]
	T = 10
	dt = 0.1

	#2f)
	pen2f = Pendulum(g=9.81, L=2.2, M=1.)
	pen2f.solve(y0, T, dt, angles = "rad")
	plt.plot(pen2f.t, pen2f.theta)
	plt.show()
	plt.plot(pen2f.t, pen2f.kinetic)
	plt.plot(pen2f.t, pen2f.potential)
	plt.plot(pen2f.t, pen2f.kinetic+pen2f.potential)
	plt.show()

	#2e
	pen2e = DampenedPendulum(g=9.81, L=2.2, M=1., B=0.9)
	pen2e.solve(y0, T , dt, angles = "rad")
	plt.plot(pen2e.t, pen2e.kinetic+pen2e.potential)
	plt.show()



