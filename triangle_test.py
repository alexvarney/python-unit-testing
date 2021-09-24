import unittest


def square(x):
  return x ** 2

def exists_right_triangle(x: float, y: float, z: float) -> bool:
  
  squares = sorted(map(square, (x, y, z)))
  return abs(((squares[0] + squares[1]) - squares[2])) < 0.01

def exists_triangle(x, y, z):
  return sorted((x, y, z))[2] <= sorted((x,y,z))[1] + sorted((x, y, z))[0]


class TriangleTests(unittest.TestCase):
  def test_right_triangle(self):

    #do whatever you want

    self.assertFalse(exists_right_triangle(1.0, 1.0, 1.0))
    self.assertFalse(exists_right_triangle(1, 2, 9))
    self.assertTrue(exists_right_triangle(4, 8, 8.94427191))
    self.assertTrue(exists_right_triangle(5, 12, 13))

  def test_any_triangle(self):
    self.assertTrue(exists_triangle(1.0, 1.0, 1.0))
    self.assertFalse(exists_triangle(1, 2, 9))
    self.assertTrue(exists_triangle(4, 8, 8.94427191))
    self.assertTrue(exists_triangle(5, 12, 13))
    

if __name__ == '__main__':
  unittest.main()