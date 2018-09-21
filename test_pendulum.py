from pendulum import Pendulum
import numpy as np
import nose.tools as nt

def test_solve():
	y0 = [np.pi/4., 0.1]
	T = 10
	dt = 0.1
	pen = Pendulum(g=9.81, L=2.2, M=1.)
	pen.solve([0.0, 0.0], T, dt, angles = "deg")
	for i in range(len(pen.t)):
		nt.assert_equal(pen.theta, 0)

test_solve()

if __name__ == '__main__':
	import nose
	nose.run()