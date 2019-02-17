# note that only modules can be imported relatively
# from . explainerrors import ExplainErrors did not work because 01_PythonErrors is not a module (does not have __init__.py)
from fizzbuzz import fizzbuzz as fz
from unittest import TestCase

class test_fiz(TestCase):

    def test_input_type(self):
        with self.assertRaises(TypeError):
            fz(start_no='asdf',stop_no=[234234])

    def test_check_0_100(self):
        expected =  "Fizz    :3\n" \
                    "Buzz    :5\n" \
                    "Fizz    :6\n" \
                    "Fizz    :9\n" \
                    "Buzz    :10\n" \
                    "Fizz    :12\n" \
                    "FizzBuzz:15\n" \
                    "Fizz    :18\n" \
                    "Buzz    :20\n" \
                    "Fizz    :21\n" \
                    "Fizz    :24\n" \
                    "Buzz    :25\n" \
                    "Fizz    :27\n" \
                    "FizzBuzz:30\n" \
                    "Fizz    :33\n" \
                    "Buzz    :35\n" \
                    "Fizz    :36\n" \
                    "Fizz    :39\n" \
                    "Buzz    :40\n" \
                    "Fizz    :42\n" \
                    "FizzBuzz:45\n" \
                    "Fizz    :48\n" \
                    "Buzz    :50\n" \
                    "Fizz    :51\n" \
                    "Fizz    :54\n" \
                    "Buzz    :55\n" \
                    "Fizz    :57\n" \
                    "FizzBuzz:60\n" \
                    "Fizz    :63\n" \
                    "Buzz    :65\n" \
                    "Fizz    :66\n" \
                    "Fizz    :69\n" \
                    "Buzz    :70\n" \
                    "Fizz    :72\n" \
                    "FizzBuzz:75\n" \
                    "Fizz    :78\n" \
                    "Buzz    :80\n" \
                    "Fizz    :81\n" \
                    "Fizz    :84\n" \
                    "Buzz    :85\n" \
                    "Fizz    :87\n" \
                    "FizzBuzz:90\n" \
                    "Fizz    :93\n" \
                    "Buzz    :95\n" \
                    "Fizz    :96\n" \
                    "Fizz    :99\n" \
                    "Buzz    :100\n"

        self.assertEqual(fz(), expected)

    def test_check_other_input(self):
        expected =  "Buzz    :-10\n" \
                    "Fizz    :-9\n" \
                    "Fizz    :-6\n" \
                    "Buzz    :-5\n" \
                    "Fizz    :-3\n" \
                    "Fizz    :3\n" \
                    "Buzz    :5\n" \
                    "Fizz    :6\n" \
                    "Fizz    :9\n" \
                    "Buzz    :10\n"

        self.assertEqual(fz(start_no=-10, stop_no=10), expected)

    def test_zero(self):
        self.assertEqual(fz(0,0), "")
