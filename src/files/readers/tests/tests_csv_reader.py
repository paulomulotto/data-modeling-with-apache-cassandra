import os
import unittest
import pandas as pd
from src.files.readers.csv_reader import CSVReader
from src.files.readers.validators.rules import NotNullOrEmptyRule


class TestCSVReader(unittest.TestCase):
    """
    Test cases for CSVReader class.
    """

    def setUp(self):
        self.test_file = 'test.csv'
        with open(self.test_file, 'w') as f:
            f.write("id,name,age\n")
            f.write("1,John,25\n")
            f.write("2,Jane,30\n")

        self.empty_file = 'empty.csv'
        open(self.empty_file, 'a').close()  # Create an empty file

        self.header_only_file = 'header_only.csv'
        with open(self.header_only_file, 'w') as f:
            f.write("id,name,age\n")

        self.csv_reader = CSVReader(
            [
                self.test_file,
                self.header_only_file
            ]
        )

    def tearDown(self):
        os.remove(self.test_file)
        os.remove(self.empty_file)
        os.remove(self.header_only_file)

    def test_read_file(self):
        """
        Test reading data from a CSV file.
        """
        self.assertEqual(self.csv_reader.get_data_length(), 2)
        self.assertEqual(len(self.csv_reader.get_data()), 2)
        self.assertEqual(self.csv_reader.get_data().iloc[0].tolist(), [1, "John", 25])  # Assert that the first line of data was read correctly
        self.assertEqual(self.csv_reader.get_data().iloc[1].tolist(), [2, "Jane", 30])  # Assert that the second line of data was read correctly

    def test_invalid_file(self):
        """
        Test reading an invalid file.
        """
        with self.assertRaises(FileNotFoundError):  # Assert that a FileNotFoundError is raised when trying to read an invalid file
            self.csv_reader.read_file('invalid.csv')

    def test_empty_file(self):
        """
        Test reading an empty file.
        """
        with self.assertRaises(ValueError):
            self.csv_reader.read_file(self.empty_file)

    def test_no_data_in_file(self):
        """
        Test reading a file with no data, only containing the header.
        """
        csv_reader = CSVReader([self.header_only_file])
        self.assertTrue(csv_reader.get_data().empty)  # Assert that the DataFrame is empty

    def test_nonexistent_file(self):
        """
        Test reading a file that does not exist.
        """
        nonexistent_file = 'nonexistent.csv'
        with self.assertRaises(FileNotFoundError):
            self.csv_reader.read_file(nonexistent_file)


if __name__ == '__main__':
    unittest.main()
