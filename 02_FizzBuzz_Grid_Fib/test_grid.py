# note that only modules can be imported relatively
# from . explainerrors import ExplainErrors did not work because 01_PythonErrors is not a module (does not have __init__.py)
from grid import draw_grid as dg
from unittest import TestCase


class test_grid(TestCase):

    def test_input_type(self):
        with self.assertRaises(TypeError):
            dg(row="", col="", size="")

    def test_grid(self):
        draw1x1x1 = "+-+\n" \
                    "| |\n" \
                    "+-+"
        draw2x1x1 = "+-+\n" \
                    "| |\n" \
                    "+-+\n" \
                    "| |\n" \
                    "+-+"
        draw1x2x1 = "+-+-+\n" \
                    "| | |\n" \
                    "+-+-+"
        draw1x1x2 = "+--+\n" \
                    "|  |\n" \
                    "|  |\n" \
                    "+--+"

        self.assertEqual(dg(1, 1, 1), draw1x1x1)
        self.assertEqual(dg(2, 1, 1), draw2x1x1)
        self.assertEqual(dg(1, 2, 1), draw1x2x1)
        self.assertEqual(dg(1, 1, 2), draw1x1x2)
