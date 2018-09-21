
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class DoublePendulum:
    def __init__(self, g = 9.81 , L1 = 1., L2=1., M1=1., M2 = 1.):
        """g is gravity, L1 and L2 is length of pendulums, M1 and M2 is mass of pendulums. """
        self.g = g
        self.L1 = L1
        self.L2 = L2
        self.M1 = M1
        self.M2 = M2

    def __call__(self, t, y):
        """ Returns derivatives as array of theta1, theta2 and omega1, omega2 values."""
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
        """
        Method takes in the initial value, end of interval and size of increment. 
        The last arguments specifies if the angle is given in degrees or radians.
        Returns theta1, omega1, theta2, omega2 and t as arrays.
        """
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
        """Plots animation."""
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
        """Returns coordinates. """
        self.pendulums.set_data((0, self.x1[i], self.x2[i]),
                                (0, self.y1[i], self.y2[i]))
        return self.pendulums,

    def show_animation(self):
        """Shows animation """
        plt.show()

    def save_animation(self, filename):
        """ Saves animation in given filename. """
        self.animation.save(filename, fps=60, writer = "mencoder")

    @property
    def t(self):
        """ Returns array of t's."""
        try:
            return self._t
        except AttributeError:
            print("Must use method solve first.")
            raise 

    @property
    def theta1(self):
        """ Returns array of theta1s."""
        try:
            return self._theta1
        except AttributeError:
            print("Must use method solve first.")
            raise

    @property
    def theta2(self):
        """ Returns array of theta2's."""
        try:
            return self._theta2
        except AttributeError:
            print("Must use method solve first.")
            raise

    @property 
    def x1(self):
        """ Returns array of x1's."""
        self._x1 = self.L1 * np.sin(self._theta1)
        return self._x1

    @property
    def y1(self):
        """ Returns array of y1's."""
        self._y1 = -self.L1 * np.cos(self._theta1)
        return self._y1

    @property 
    def x2(self):
        """ Returns array of x2's."""
        self._x2 = self._x1 + self.L2 * np.sin(self._theta2)
        return self._x2

    @property
    def y2(self):
        """ Returns array of y2's."""
        self._y2 = self.y1 -self.L2 * np.cos(self._theta2)
        return self._y2

    @property
    def potential(self):
        """ Returns potential energy as array."""
        p1 = self.M1*self.g*(self.y1+self.L1)
        p2 = self.M2*self.g*(self.y2+self.L1 + self.L2)
        self._p = p1 + p2
        return self._p

    @property 
    def vx1(self):
        """ Returns velocity vx1 as an array."""
        self._vx1 = np.gradient(self.x1, self.t)
        return self._vx1

    @property 
    def vy1(self):
        """ Returns velocity vy1 as an array."""
        self._vy1 = np.gradient(self.y1, self.t)
        return self._vy1

    @property 
    def vx2(self):
        """ Returns velocity vx2 as an array."""
        self._vx2 = np.gradient(self.x2, self.t)
        return self._vx2

    @property 
    def vy2(self):
        """ Returns velocity vy2 as an array."""
        self._vy2 = np.gradient(self.y2, self.t)
        return self._vy2

    @property 
    def kinetic(self):
        """ Returns kinetic energy as an array."""
        K1 = 1./2 * self.M1 * (np.square(self.vx1) + np.square(self.vy1))
        K2 = 1./2 * self.M2 * (np.square(self.vx2) + np.square(self.vy2))
        self._K = K1 + K2
        return self._K

if __name__ == "__main__":
    # Test runs:

    y0 = [np.pi, 0.1, np.pi/2., 0.1]
    T = 10.
    dt = 0.01

    pen = DoublePendulum()
    pen.solve(y0, T , dt, angles = "rad")
    plt.plot(pen.t, pen.kinetic)
    plt.plot(pen.t, pen.potential)
    plt.plot(pen.t, pen.kinetic+pen.potential)
    plt.show()

    pen.create_animation()
    pen.show_animation()
    pen.save_animation("animation_double_pendulum.mp4")
