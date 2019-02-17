# note that only modules can be imported relatively
# from . explainerrors import ExplainErrors did not work because 01_PythonErrors is not a module (does not have __init__.py)
from series import added_series
from unittest import TestCase


class test_series(TestCase):

    def test_input_type(self):
        with self.assertRaises(TypeError):
            added_series(term1="", term2="", nth_term="")

    def test_bad_input(self):
        with self.assertRaises(ValueError):
            added_series(nth_term=-1)

    def test_fib(self):
        self.assertEqual(added_series(term1=0, term2=1, nth_term=1), 0)
        self.assertEqual(added_series(term1=0, term2=1, nth_term=2), 1)
        self.assertEqual(added_series(term1=0, term2=1, nth_term=3), 1)
        self.assertEqual(added_series(term1=0, term2=1, nth_term=4), 2)
        self.assertEqual(added_series(term1=0, term2=1, nth_term=5), 3)
        self.assertEqual(added_series(term1=0, term2=1, nth_term=6), 5)

    def test_lucas(self):
        self.assertEqual(added_series(term1=2, term2=1, nth_term=1), 2)
        self.assertEqual(added_series(term1=2, term2=1, nth_term=2), 1)
        self.assertEqual(added_series(term1=2, term2=1, nth_term=3), 3)
        self.assertEqual(added_series(term1=2, term2=1, nth_term=4), 4)
        self.assertEqual(added_series(term1=2, term2=1, nth_term=5), 7)
        self.assertEqual(added_series(term1=2, term2=1, nth_term=6), 11)