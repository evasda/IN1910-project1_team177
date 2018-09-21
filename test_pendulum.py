from exp_decay import ExponentialDecay
import nose.tools as nt

def test_solve():
	pen = Pendulum(g=9.81, L=2.2, M=1.)
	pen.solve(y0, T , dt, angles = "rad")
	t1, y1 = pen.solve([0.0, 0.0], T, dt, angles = "deg")
	nt.assert_equal(y1, 0)

test_solve()

if __name__ == '__main__':
	import nose
	nose.run()