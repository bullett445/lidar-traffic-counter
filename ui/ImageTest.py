import unittest
from ui.DisplayImage import DisplayImage


class MyTestCase(unittest.TestCase):
    def test_something(self):
        img = DisplayImage()
        img.drawBar(15, 1.0, 'yellow')
        img.drawBarMark(15, 0.6, 'red')
        img.drawBar(35, 0.4, 'white')
        img.drawState(5, 50, 'pause')
        img.writeSpeed(36, 60, '55')
        img.debugShow()


if __name__ == '__main__':
    unittest.main()
