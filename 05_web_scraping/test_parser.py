import unittest
import parser.parse


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')
