import unittest
from sierpinski_points import midpoint
from typing import Tuple

class SierpinskiPointsTest(unittest.TestCase):
    def test_midpoint_x_only(self):
        x0 = (0., 0.)
        x1 = (1., 0.)
        self.assertTupleAlmostEqual(midpoint(x0, x1), (0.5, 0.))

    def test_midpoint_y_only(self):
        x0 = (0., 1.)
        x1 = (0., 0.)
        self.assertTupleAlmostEqual(midpoint(x0, x1), (0., 0.5))

    def test_midpoint_x_and_y(self):
        x0 = (0.8, 1.)
        x1 = (-2, -0.5)
        self.assertTupleAlmostEqual(midpoint(x0, x1), (-0.6, 0.25))

    def assertTupleAlmostEqual(self, t0: Tuple, t1: Tuple):
        self.assertTrue(len(t0) == len(t1))

        for tt0, tt1 in zip(t0, t1):
            self.assertAlmostEqual(tt0, tt1)


if __name__ == '__main__':
    unittest.main()
