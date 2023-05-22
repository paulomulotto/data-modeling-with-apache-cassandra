import unittest
from unittest.mock import patch
from libs.files.collector import FileCollector


class TestFileCollector(unittest.TestCase):
    @patch('os.walk')
    @patch('glob.glob')
    def test_collect_files(self, mock_glob, mock_walk):
        # Set up the mock return values
        mock_walk.return_value = [
            ('/path/to/test_directory', [], ['file1.txt']),
            ('/path/to/test_directory/subdir', [], ['file2.txt'])
        ]
        mock_glob.return_value = ['/path/to/test_directory/file1.txt', '/path/to/test_directory/subdir/file2.txt']

        # Create an instance of FileCollector
        file_collector = FileCollector('/path/to/test_directory')

        # Collect the files
        files = file_collector.collect_files()

        # Check the collected files
        expected_files = {
            '/path/to/test_directory/file1.txt',
            '/path/to/test_directory/subdir/file2.txt'
        }
        self.assertSetEqual(set(files), expected_files)

    @patch('os.walk')
    @patch('glob.glob')
    def test_collect_files_empty_directory(self, mock_glob, mock_walk):
        # Set up the mock return values for an empty directory
        mock_walk.return_value = []
        mock_glob.return_value = []

        # Create an instance of FileCollector
        file_collector = FileCollector('/path/to/empty_directory')

        # Collect the files
        files = file_collector.collect_files()

        # Check that no files are collected
        self.assertEqual(len(files), 0)


if __name__ == '__main__':
    unittest.main()
