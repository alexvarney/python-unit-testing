import unittest


def sqrt(value: int):
  return value ** 0.5


class SqrtTesting(unittest.TestCase):
    
    def test_sqrt(self):
      self.assertEqual(sqrt(4), 2)
      self.assertEqual(sqrt(9), 3)

    def another_test(self):
      self.assertEqual(sqrt(25), 5)
      self.assertEqual(sqrt(144), 12)
      self.assertEqual(sqrt(1023), 32)



if __name__ == '__main__':
    unittest.main()