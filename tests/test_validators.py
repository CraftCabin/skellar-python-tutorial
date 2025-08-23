import unittest
from src.validators.base_validator import BaseValidator
from src.validators.python_runner import PythonRunner

class TestValidators(unittest.TestCase):

    def setUp(self):
        self.validator = BaseValidator()
        self.runner = PythonRunner()

    def test_base_validator(self):
        # Example test for BaseValidator
        self.assertTrue(self.validator.is_valid("test"))

    def test_python_runner_execution(self):
        # Example test for PythonRunner
        code = "print('Hello, World!')"
        expected_output = "Hello, World!"
        output = self.runner.run(code)
        self.assertEqual(output.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()