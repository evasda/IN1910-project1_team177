from exp_decay import ExponentialDecay
import nose.tools as nt

def test_call():
	"""Test that the call method returns correct derivative for known function."""
    a = 0.4
    ut = 3.2
    ED = ExponentialDecay(a)
    deriv = ED(1, ut)
    nt.assert_equal(deriv, -1.28)

test_call()

if __name__ == '__main__':
	import nose
	nose.run()
