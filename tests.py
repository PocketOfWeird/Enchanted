import unittest
from modules.touch_manager import touch_manager

class TestTouchManager(unittest.TestCase):

    def test_manager_input(self):
        expected = ["sb_dubdeuce.mp3","sb_system.mp3","sb_pizza.mp3"]
        result = touch_manager(2)
        self.assertIn(result, expected)

unittest.main()
