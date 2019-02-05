# note that only modules can be imported relatively
# from . explainerrors import ExplainErrors did not work because 01_PythonErrors is not a module (does not have __init__.py)
from explainerrors import ExplainErrors as exp
from unittest import TestCase

class test_errors(TestCase):

    def test_syntax(self):
        with self.assertRaises(SyntaxError):
            exp.throw_syntax()

    def test_type(self):
        with self.assertRaises(TypeError):
            exp.throw_type()

    def test_index(self):
        with self.assertRaises(IndexError):
            exp.throw_index()

    def test_key(self):
        with self.assertRaises(KeyError):
            exp.throw_key()

    def test_attribute(self):
        with self.assertRaises(AttributeError):
            exp.throw_attribute()