import abc
from typing import Dict, Any


class BaseTableManager(abc.ABC):
    """
    Abstract base class for table managers.
    """

    def __init__(self, connector):
        self.connector = connector

    @abc.abstractmethod
    def create_table(self, table_name: str, columns: Dict[str, str]) -> None:
        """
        Create a table with the specified name and columns.

        Args:
            table_name: The name of the table to create.
            columns: A dictionary of column names and their data types.
        """

    @abc.abstractmethod
    def insert_data(self, table_name: str, data: Dict[str, Any]) -> None:
        """
        Insert data into the specified table.

        Args:
            table_name: The name of the table to insert data into.
            data:
                A dictionary representing the data to insert,
                where the keys are column names and the values
                are the corresponding data values.
        """

    @abc.abstractmethod
    def drop_table(self, table_name: str) -> None:
        """
        Drop the specified table.

        Args:
            table_name: The name of the table to drop.
        """
