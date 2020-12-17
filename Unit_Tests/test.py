import unittest

import inc_dec    # The code to test

class IncrementDecrementTests(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(inc_dec.increment(3), 4)

    def test_decrement(self):
        self.assertEqual(inc_dec.decrement(3), 2)
    
    def test_always_fail(self):
        self.assertEqual(1, 1)
    
    def test_always_pass(self):
        self.assertEqual(12, 12)
    
    def test_always_fails_1(self):
        self.assertEqual(21, 12)
        

if __name__ == '__main__':
    unittest.main()