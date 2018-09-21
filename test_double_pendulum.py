from double_pendulum import DoublePendulum
import numpy as np
import nose.tools as nt

def test_call():
	T = 10
	dt = 0.1
	pend = DoublePendulum()
	theta1, omega1, theta2, omega2 = pend(0.0, [0.0, 0.0, 0.0, 0.0])
	nt.assert_equal(theta1, 0.0)
	nt.assert_equal(omega1, 0.0)
	nt.assert_equal(theta2, 0.0)
	nt.assert_equal(omega2, 0.0)


def test_solve():
	T = 10
	dt = 0.1
	pend = DoublePendulum()
	pend.solve([0.0, 0.0, 0.0, 0.0], T, dt, angles = "deg")
	t_act = np.linspace(0, T, int(T/dt))
	print(pend.t)
	for i in range(len(t_act)):
		nt.assert_equal(pend.theta1[i], 0.)
		nt.assert_equal(pend.theta2[i], 0.)
		nt.assert_equal(pend.t[i], t_act[i])

@nt.raises(AttributeError)
def test_t():
	pen = DoublePendulum()
	pen.t

@nt.raises(AttributeError)
def test_theta1():
	pen = DoublePendulum()
	pen.theta1

@nt.raises(AttributeError)
def test_theta2():
	pen = DoublePendulum()
	pen.theta2


if __name__ == '__main__':
	import nose
	nose.run()