from src.files.writers.csv import CSVWriter


class WriterFactory:
    """
    Factory class for creating different types of writers.
    """

    @staticmethod
    def create_writer(file_path, writer_type='csv', **kwargs):
        """
        Create a writer based on the specified writer type.

        :param file_path: The path of the file to write.
        :param writer_type: The type of writer to create (default is 'csv').
        :param kwargs: Additional keyword arguments to pass to the writer constructor.
        :return: An instance of the specified writer type.
        :raises ValueError: If an unsupported writer type is specified.
        """
        if writer_type == 'csv':
            return CSVWriter(file_path, **kwargs)
        else:
            raise ValueError(f"Unsupported writer type: {writer_type}")