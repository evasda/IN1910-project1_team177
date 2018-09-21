
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class DoublePendulum:
    def __init__(self, g = 9.81 , L1 = 1., L2=1., M1=1., M2 = 1.):
        self.g = g
        self.L1 = L1
        self.L2 = L2
        self.M1 = M1
        self.M2 = M2

    def __call__(self, t, y):
        g = self.g
        L1 = self.L1
        L2 = self.L2
        M1 = self.M1
        M2 = self.M2
        deriv_omega1 = (-g*(2*M1+M2)*np.sin(y[0]) - M2*g*np.sin(y[0]-2*y[2]) - 2*np.sin(y[0]-y[2]) *M2*(y[3]**2*L2+y[1]**2*L1*np.cos(y[0]-y[2]))) / (L1*(2*M1+M2 -M2*np.cos(2*y[0]-2*y[2])))
        deriv_omega2 = (2*np.sin(y[0]-y[2]) * (y[1]**2 *L1*(M1+M2)+g*(M1+M2)*np.cos(y[0]) + y[3]**2*L2 * M2*np.cos(y[0]-y[2])))/ (L2*(2*M1+M2 -M2*np.cos(2*y[0]-2*y[2])))
        deriv_theta1 = y[1]
        deriv_theta2 = y[3]
        return [deriv_theta1, deriv_omega1, deriv_theta2, deriv_omega2]

    def solve(self, y0, T, dt, angles):
        """Method takes in the derivative, initial value, end of interval and size of increment. The last arguments specifies if the angle is given in degrees or radians."""
        if angles == "deg":
            y0[0] = y0[0]* np.pi/180.
            y0[1] = y0[1]*np.pi/180.
            y0[2] = y0[2]* np.pi/180.
            y0[3] = y0[3]* np.pi/180.
        sol = solve_ivp(self.__call__, [0,T], y0, t_eval = list(np.linspace(0, T, T/dt)), method = "Radau")
        self._theta1 = sol.y[0]; self._omega1= sol.y[1]; self._theta2=sol.y[2]; self._omega2 = sol.y[3]
        self._t = sol.t
        self.dt = dt

    def create_animation(self):
        # Create empty figure
        fig = plt.figure()
        
        # Configure figure
        plt.axis('equal')
        plt.axis('off')
        plt.axis((-3, 3, -3, 3))

        # Make an "empty" plot object to be updated throughout the animation
        self.pendulums, = plt.plot([], [], 'o-', lw=2)

        # Call FuncAnimation
        self.animation = animation.FuncAnimation(fig,
                                                 self._next_frame,
                                                 frames=range(len(self.x1)), 
                                                 repeat=None,
                                                 interval=1000*self.dt, 
                                                 blit=True)

    def _next_frame(self, i):
        self.pendulums.set_data((0, self.x1[i], self.x2[i]),
                                (0, self.y1[i], self.y2[i]))
        return self.pendulums,

    def show_animation(self):
        plt.show()

    @property
    def t(self):
        return self._t

    @property
    def theta1(self):
        return self._theta1

    @property
    def theta2(self):
        return self._theta2

    @property 
    def x1(self):
        self._x1 = self.L1 * np.sin(self._theta1)
        return self._x1

    @property
    def y1(self):
        self._y1 = -self.L1 * np.cos(self._theta1)
        return self._y1

    @property 
    def x2(self):
        self._x2 = self._x1 + self.L2 * np.sin(self._theta2)
        return self._x2

    @property
    def y2(self):
        self._y2 = self.y1 -self.L2 * np.cos(self._theta2)
        return self._y2

    @property
    def potential(self):
        p1 = self.M1*self.g*(self.y1+self.L1)
        p2 = self.M2*self.g*(self.y2+self.L1 + self.L2)
        self._p = p1 + p2
        return self._p

    @property 
    def vx1(self):
        self._vx1 = np.gradient(self.x1, self.t)
        return self._vx1

    @property 
    def vy1(self):
        self._vy1 = np.gradient(self.y1, self.t)
        return self._vy1

    @property 
    def vx2(self):
        self._vx2 = np.gradient(self.x2, self.t)
        return self._vx2

    @property 
    def vy2(self):
        self._vy2 = np.gradient(self.y2, self.t)
        return self._vy2

    @property 
    def kinetic(self):
        K1 = 1./2 * self.M1 * (np.square(self.vx1) + np.square(self.vy1))
        K2 = 1./2 * self.M2 * (np.square(self.vx2) + np.square(self.vy2))
        self._K = K1 + K2
        return self._K

# Test runs:

y0 = [np.pi, 0.1, np.pi/2., 0.1]
T = 10
dt = 0.01

pen = DoublePendulum()
pen.solve(y0, T , dt, angles = "rad")
plt.plot(pen.t, pen.kinetic)
plt.plot(pen.t, pen.potential)
plt.plot(pen.t, pen.kinetic+pen.potential)
plt.show()

pen.create_animation()
pen.show_animation()