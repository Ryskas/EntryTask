import unittest
from test_csv import TestCSV

test_cases = unittest.TestLoader().loadTestsFromTestCase(TestCSV)

test_suite = unittest.TestSuite()
test_suite.addTests(test_cases)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
