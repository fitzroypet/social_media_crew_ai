import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import validate_inputs

class TestInputValidation(unittest.TestCase):
    def test_empty_inputs(self):
        errors = validate_inputs("", "")
        self.assertEqual(len(errors), 2)
        self.assertIn("Content topic is required", errors)
        self.assertIn("Target audience is required", errors)

    def test_short_inputs(self):
        errors = validate_inputs("ab", "test")
        self.assertEqual(len(errors), 2)
        self.assertIn("Content topic must be at least 3 characters long", errors)
        self.assertIn("Target audience description must be at least 5 characters long", errors)

    def test_valid_inputs(self):
        errors = validate_inputs("sustainable fashion", "environmentally conscious millennials")
        self.assertEqual(len(errors), 0)

if __name__ == '__main__':
    unittest.main() 