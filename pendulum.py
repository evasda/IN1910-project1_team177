import os
os.chdir("C:\\Users\\Eva\Desktop\\IN1910\\Prosjekt 1\\project1_team177\\")

from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

class Pendulum:
	def __init__(self, g = 9.81 , L = 1., M = 1.):
		self.g = g
		self.L = L
		self.M = M

	def __call__(self, t, y):
		g = self.g
		L = self.L
		deriv_omega = -(g/L)*np.sin(y[0])
		deriv_theta = y[1]
		return [deriv_theta, deriv_omega]

	def solve(self, y0, T, dt, angles):
		"""Method takes in the derivative, initial value, end of interval and size of increment. The last arguments specifies if the angle is given in degrees or radians."""
		if angles == "deg":
			y0[0] = y0[0]* np.pi/180.
			y0[1] = y0[1]*np.pi/180.
		sol = solve_ivp(self.__call__, [0,T], y0, t_eval = list(np.linspace(0, T, T/dt)))
		self._omega = sol.y[1]; self._theta = sol.y[0]
		self._t = sol.t

	@property
	def t(self):
		print("Setting t values")
		return self._t

	@property
	def theta(self):
		print("Getting theta values")
		return self._theta

	@property 
	def omega(self):
		print("Getting omega values")
		return self._omega

	@property 
	def x(self):
		print("x coordinates")
		self._x = self.L * np.sin(self._theta)
		return self._x

	@property
	def y(self):
		print("y coordinates")
		self._y = -self.L * np.cos(self._theta)
		return self._y


	@property
	def p(self):
		self._p = self.M*self.g*(self.y+self.L)
		return self._p

	@property 
	def vx(self):
		self._vx = np.gradient(self.x, self.t)
		return self._vx

	@property 
	def vy(self):
		self._vy = np.gradient(self.y, self.t)
		return self._vy

	@property 
	def kinetic(self):
		self._K = 1./2 * self.M * (np.square(self.vx) + np.square(self.vy))
		return self._K


class DampenedPendulum(Pendulum):
	def __init__(self, g = 9.81 , L = 1., M = 1., B=1.):
		self.g = g
		self.L = L
		self.M = M
		self.B = B

	def __call__(self, t, y):
		g = self.g
		L = self.L
		B = self.B
		M = self.M
		deriv_omega = -(g/L)*np.sin(y[0]) - (B/M)*y[1]
		deriv_theta = y[1]
		return [deriv_theta, deriv_omega]






y0 = [np.pi/4., 0.1]
T = 10
dt = 0.1

pen = Pendulum(g=9.81, L=2.2, M=1.)
pen.solve(y0, T , dt, angles = "rad")
#t1, y1 = pen.solve([0.0, 0.0], T, dt, angles = "deg")

#2f)
pen2f = Pendulum(g=3.711, L=2.2, M=1.)
pen2f.solve(y0, T, dt, angles = "rad")
plt.plot(pen.t, pen.theta)
plt.show()
plt.plot(pen2f.t, pen2f.theta)
plt.show()
plt.plot(pen.t, pen.kinetic)
plt.plot(pen.t, pen.p)
plt.plot(pen.t, pen.kinetic+pen.p)
plt.show()
plt.plot(pen2f.t, pen2f.kinetic)
plt.plot(pen2f.t, pen2f.p)
plt.plot(pen2f.t, pen2f.kinetic+pen2f.p)
plt.show()

#2e
pen2e = DampenedPendulum(g=9.81, L=2.2, M=1., B=2.)
pen2e.solve(y0, T , dt, angles = "rad")
plt.plot(pen2e.t, pen2e.kinetic+pen2e.p)
plt.show()

#print(pen.t)
#print(pen.theta)
#print(pen.omega)
#print(pen.y)
#print(pen.x)
print(pen.p)
print(pen.vx)
print(pen.kinetic)
#print(t1, y1)


