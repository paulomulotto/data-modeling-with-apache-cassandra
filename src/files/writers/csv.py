import os
import pandas as pd
from src.files.writers.base import BaseWriter


class CSVWriter(BaseWriter):
    """
    Writer class for writing data to a CSV file.
    """

    def __init__(self, encoding: str = 'utf8', sep: str = ','):
        """
        Initialize a new instance of CSVWriter.

        :param encoding: The encoding of the CSV file (default is 'utf8').
        :param sep: The separator to use in the CSV file (default is ',').
        :param **kwargs: Additional keyword arguments to pass to the pandas to_csv function.
        """
        super().__init__(encoding=encoding)
        self.sep = sep

    def write_data(self, file_path: str, data: pd.DataFrame, columns: list[str] = None) -> None:
        """
        Write data to the CSV file.

        :param file_path: The path of the CSV file to write.
        :param data: The data rows to write as a pandas DataFrame.
        :param columns: The columns to include in the output (default is None, which includes all columns).
        """
        directory = os.path.dirname(file_path)
        os.makedirs(directory, exist_ok=True)

        if columns is not None:
            data = data[columns]

        data.to_csv(file_path, sep=self.sep, index=False, encoding=self.encoding)
        return data
