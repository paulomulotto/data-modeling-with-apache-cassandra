import unittest
from src.databases.connectors.base import DatabaseConnector
from abc import ABC


class TestDatabaseConnector(unittest.TestCase):
    def test_abstract_class(self):
        # Check if DatabaseConnector is still an abstract class
        self.assertTrue(issubclass(DatabaseConnector, ABC))