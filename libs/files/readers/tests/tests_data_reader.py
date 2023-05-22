import unittest
from libs.files.readers.csv_reader import BaseReader


class TestDataReaders(unittest.TestCase):
    def test_cannot_instantiate_DataReader(self):
        with self.assertRaises(TypeError):
            reader = BaseReader(['test_data/test_file.txt'])

    def test_read_file(self):
        # Create a subclass of DataReader for testing purposes
        class DataReaderMock(BaseReader):
            def read_file(self, file_path):
                # Implement a mock read_file method for testing
                self.data.append("Test data")

        # Instantiate the DataReaderMock and call the read_file method
        reader = DataReaderMock([])
        reader.read_file("test_file.txt")

        # Assert that the data was properly populated
        self.assertEqual(reader.data, ["Test data"])
