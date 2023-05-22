import unittest
import os
import pandas as pd
from unittest.mock import patch
from libs.files.writers.csv import CSVWriter


class TestCSVWriter(unittest.TestCase):
    def setUp(self):
        self.writer = CSVWriter()

    @patch('os.makedirs')
    @patch('pandas.DataFrame.to_csv')
    def test_write_data_with_all_columns(self, mock_to_csv, mock_makedirs):
        # Set up the mock objects
        mock_makedirs.return_value = None
        mock_to_csv.return_value = None

        # Define the test data
        file_path = '/path/to/test_file.csv'
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        expected_columns = None

        # Call the write_data method
        data.to_csv = mock_to_csv
        self.writer.write_data(file_path, data, columns=expected_columns)

        # Assert that the necessary functions
        # are called with the correct arguments
        mock_makedirs.assert_called_once_with(
            os.path.dirname(file_path), exist_ok=True)
        mock_to_csv.assert_called_once_with(
            file_path, sep=',', index=False, encoding='utf8')

    @patch('os.makedirs')
    @patch('pandas.DataFrame.to_csv')
    def test_write_data_with_selected_columns(self, mock_to_csv, mock_makedirs):
        # Set up the mock objects
        mock_makedirs.return_value = None
        mock_to_csv.return_value = None

        # Define the test data
        file_path = '/path/to/test_file.csv'
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        expected_columns = ['A', 'C']

        # Call the write_data method
        self.writer.write_data(file_path, data, columns=expected_columns)

        # Assert that the necessary functions
        # are called with the correct arguments
        mock_makedirs.assert_called_once_with(
            os.path.dirname(file_path), exist_ok=True)
        mock_to_csv.assert_called_once_with(
            file_path, sep=',', index=False, encoding='utf8')


if __name__ == '__main__':
    unittest.main()
