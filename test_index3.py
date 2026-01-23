import unittest
import os

def load_module_from_file(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"{filepath} not found")
    with open(filepath, 'r') as f:
        code = f.read()
    module_dict = {}
    try:
        exec(code, module_dict)
    except Exception as e:
        print(f"Error executing code from {filepath}: {e}")
        raise
    return module_dict

class TestMaxSubarraySum(unittest.TestCase):
    def setUp(self):
        self.module = load_module_from_file('index3.html')
        self.max_subarray_sum = self.module.get('max_subarray_sum')
        if not self.max_subarray_sum:
            self.fail("max_subarray_sum function not found in index3.html")

    def test_basic_example(self):
        # Example from standard Kadane's algorithm explanations
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        # Subarray [4, -1, 2, 1] sums to 6
        self.assertEqual(self.max_subarray_sum(arr), 6)

    def test_all_negative(self):
        # Should return the maximum single element (least negative)
        arr = [-5, -2, -9, -1, -8]
        self.assertEqual(self.max_subarray_sum(arr), -1)

    def test_single_element_positive(self):
        self.assertEqual(self.max_subarray_sum([5]), 5)

    def test_single_element_negative(self):
        self.assertEqual(self.max_subarray_sum([-5]), -5)

    def test_mixed_positive_negative(self):
        arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
        # Subarray [3, 4, -1, 2, 1] sums to 9
        self.assertEqual(self.max_subarray_sum(arr), 9)

    def test_empty_array(self):
        self.assertEqual(self.max_subarray_sum([]), 0)

    def test_all_positive(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(self.max_subarray_sum(arr), 15)

if __name__ == '__main__':
    unittest.main()
