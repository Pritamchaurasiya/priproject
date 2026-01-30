import unittest
import os

class TestKadane(unittest.TestCase):
    def setUp(self):
        # Read the content of index3.html
        with open('index3.html', 'r') as f:
            code = f.read()

        # Execute the code in a separate namespace
        self.namespace = {}
        exec(code, self.namespace)
        self.max_subarray_sum = self.namespace['max_subarray_sum']

    def test_mixed_numbers(self):
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(self.max_subarray_sum(arr), 6)

    def test_all_negative(self):
        arr = [-2, -5, -1, -8]
        self.assertEqual(self.max_subarray_sum(arr), -1)

    def test_all_positive(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(self.max_subarray_sum(arr), 10)

    def test_single_element_positive(self):
        arr = [5]
        self.assertEqual(self.max_subarray_sum(arr), 5)

    def test_single_element_negative(self):
        arr = [-5]
        self.assertEqual(self.max_subarray_sum(arr), -5)

    def test_empty_array(self):
        arr = []
        self.assertEqual(self.max_subarray_sum(arr), 0)

    def test_large_numbers(self):
        arr = [1000, -500, 2000, -100]
        self.assertEqual(self.max_subarray_sum(arr), 2500)

if __name__ == '__main__':
    unittest.main()
