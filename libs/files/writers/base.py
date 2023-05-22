from abc import ABC, abstractmethod


class BaseWriter(ABC):
    """
    Abstract base class for different types of writers.
    """

    def __init__(self, encoding='utf8'):
        """
        Initialize a new instance of BaseWriter.

        :param file_path: The path of the file to write.
        :param encoding: The encoding of the file (default is 'utf8').
        """
        self.encoding = encoding

    @abstractmethod
    def write_data(self, header, data):
        """
        Write data to the file.

        :param header: The header row to write.
        :param data: The data rows to write.
        """
