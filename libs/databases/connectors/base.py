from abc import ABC, abstractmethod


class DatabaseConnector(ABC):
    """
    Abstract base class for managing database connectors.
    """

    @abstractmethod
    def connect(self):
        """
        Connect to the database.
        """

    @abstractmethod
    def disconnect(self):
        """
        Disconnect from the database.
        """

    @abstractmethod
    def execute_query(self, query):
        """
        Execute a query on the database.

        :param query: The query to execute.
        """
