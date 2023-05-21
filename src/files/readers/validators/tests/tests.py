import unittest
import pandas as pd
from src.files.readers.validators.rules import NotNullOrEmptyRule
from src.files.readers.validators.column import ColumnValidator


class TestColumnValidator(unittest.TestCase):
    """
    Test cases for ColumnValidator class.
    """

    def setUp(self):
        self.data = {
            'id': [1, 2, 3],
            'name': ['John', 'Jane', ''],
            'age': [25, 30, 35]
        }
        self.df = pd.DataFrame(self.data)

    def test_valid_columns(self):
        """
        Test validation of valid columns.
        """
        rules = {
            'id': NotNullOrEmptyRule(),
            'name': NotNullOrEmptyRule(),
            'age': NotNullOrEmptyRule()
        }
        validator = ColumnValidator(rules, self.df)
        validation_results = validator.validate(self.df)

        expected_results = {
            'id': True,
            'name': True,
            'age': True
        }

        self.assertEqual(validation_results, expected_results)

    def test_invalid_columns(self):
        """
        Test validation of invalid columns.
        """
        rules = {
            'id': NotNullOrEmptyRule(),
            'email': NotNullOrEmptyRule(),
            'age': NotNullOrEmptyRule()
        }
        with self.assertRaises(ValueError):
            ColumnValidator(rules, self.df)

    def test_multiple_rules(self):
        """
        Test validation with multiple rules for a column.
        """
        rules = {
            'id': [NotNullOrEmptyRule()],
            'name': NotNullOrEmptyRule(),
            'age': NotNullOrEmptyRule()
        }
        validator = ColumnValidator(rules, self.df)
        validation_results = validator.validate(self.df)

        expected_results = {
            'id': True,
            'name': True,
            'age': True
        }

        self.assertEqual(validation_results, expected_results)

    def test_empty_dataframe(self):
        """
        Test validation with an empty DataFrame.
        """
        rules = {
            'id': NotNullOrEmptyRule(),
            'name': NotNullOrEmptyRule(),
            'age': NotNullOrEmptyRule()
        }
        empty_df = pd.DataFrame()
        validator = ColumnValidator(rules, empty_df)
        validation_results = validator.validate(empty_df)

        expected_results = {}

        self.assertEqual(validation_results, expected_results)


if __name__ == '__main__':
    unittest.main()
