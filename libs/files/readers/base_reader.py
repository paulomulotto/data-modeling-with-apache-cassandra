import abc


class BaseReader(abc.ABC):
    """
    Abstract base class for a data reader.
    """

    def __init__(self, file_paths, data=[]):
        """
        Initialize a new instance of DataReader.

        :param file_paths: A list of file paths to read data from.
        """
        self.file_paths = file_paths
        self.data = data
        self.read_files()

    @abc.abstractmethod
    def read_file(self, file_path):
        """
        Read data from a file. Must be implemented by subclasses.

        :param file_path: The path of the file to read.
        """

    def read_files(self):
        """
        Read data from all files in self.file_paths.
        """
        for file_path in self.file_paths:
            self.read_file(file_path)

    def get_data(self):
        """
        Get the data read from the files.

        :return: A list of data read from the files.
        """
        return self.data

    def get_data_length(self):
        """
        Get the number of data items read from the files.

        :return: The number of data items read from the files.
        """
        return len(self.data)
