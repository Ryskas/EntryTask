import unittest
import get_data
import csv
import os

class TestCSV(unittest.TestCase):

    def test_create(self):
        get_data.CreateCSV("test.csv",["123456789", "type", "state", "status"])
        self.assertTrue(os.path.exists("test.csv"))
        os.remove("test.csv")

    def test_first_row(self):
        get_data.CreateCSV("test2.csv",["123456789", "type", "state", "status"])
        with open('test2.csv', 'r') as f:
            reader = csv.reader(f)
            row = next(reader)
        self.assertEqual(row, ["Assignee","Type", "State", "Status"])
        os.remove("test2.csv")