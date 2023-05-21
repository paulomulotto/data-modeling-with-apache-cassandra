import os
import pandas as pd
from src.files.readers.base_reader import BaseReader


class CSVReader(BaseReader):
    """
    Class to read data from CSV files.
    """

    def __init__(self, file_paths, encoding='utf8'):
        """
        Initialize a new instance of CSVReader.

        :param file_paths: A list of CSV file paths to read data from.
        :param encoding: The encoding of the CSV files.
        """
        self.encoding = encoding
        super().__init__(
            file_paths,
            data=pd.DataFrame(),
        )

    def read_file(self, file_path):
        """
        Read data from a CSV file.

        :param file_path: The path of the CSV file to read.
        """
        if os.path.getsize(file_path) == 0:
            raise ValueError(f"The file '{file_path}' is empty.")

        df = pd.read_csv(file_path, encoding=self.encoding)

        self.data = pd.concat([self.data] + [df], ignore_index=True)

        # Check if the file is empty
        if self.data.empty:
            print(f"Warning: The file '{file_path}' is empty.")

    def apply_filter(self, condition):
        """
        Apply a filter to remove rows from the data DataFrame
        based on the given condition.

        :param condition: A boolean condition to filter the rows.
                          The condition should be in the form
                          of a lambda function that takes a row
                          as input and returns True if the row should
                          be kept, False otherwise.
        """
        self.data = self.data[self.data.apply(condition, axis=1)]
