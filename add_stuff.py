import unittest


def add(x, y):
  return x ** y




class TriangleTests(unittest.TestCase):
  def test_addition(self):

    #do whatever you want

    self.assertFalse(add(1.0, 2), 3)
    self.assertFalse(add(1, 2), 3)
    self.assertTrue(add(4, 8), 12)
    self.assertTrue(add(5, 1), 6)

    

if __name__ == '__main__':
  unittest.main()