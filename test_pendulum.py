from pendulum import Pendulum
import numpy as np
import nose.tools as nt

def test_call():
	"""Test that call method returns correct theta and omega."""
	T = 10
	dt = 0.1
	pen = Pendulum(g=9.81, L=2.2, M=1.)
	theta, omega = pen(0.0, [np.pi/4., 0.1])
	nt.assert_equal(theta, 0.1)
	nt.assert_equal(omega, -9.81/(2.2*np.sqrt(2)))
	thet, omeg =pen(0.0, [0.0, 0.0])
	nt.assert_equal(thet, 0.0)
	nt.assert_equal(omeg, 0.0)


def test_solve():
	"Test solve_method."
	T = 10
	dt = 0.1
	pen = Pendulum(g=9.81, L=2.2, M=1.)
	pen.solve([0.0, 0.0], T, dt, angles = "deg")
	t_act = np.linspace(0, T, int(T/dt))
	for i in range(len(pen.t)):
		nt.assert_equal(pen.theta[i], 0.)
		nt.assert_equal(pen.omega[i], 0.)
		nt.assert_equal(pen.t[i], t_act[i])


@nt.raises(AttributeError)
def test_t():
	"""Test that AttributeError is raised."""
	pen = Pendulum()
	pen.t

@nt.raises(AttributeError)
def test_theta():
	"""Test that AttributeError is raised."""
	pen = Pendulum()
	pen.theta

@nt.raises(AttributeError)
def test_omega():
	"""Test that AttributeError is raised."""
	pen = Pendulum()
	pen.omega

def test_radius():
	"""Test that length of pendulum is consistent."""
	y0 = [np.pi/4., 0.1]
	T = 10
	dt = 0.1

	pen = Pendulum(g=9.81, L=2.2, M=1.)
	pen.solve(y0, T , dt, angles = "rad")
	r_square = pen.x**2 + pen.y**2
	for i in range(len(pen.t)):
		nt.assert_almost_equal(r_square[i], 2.2**2)



if __name__ == '__main__':
	import nose
	nose.run()