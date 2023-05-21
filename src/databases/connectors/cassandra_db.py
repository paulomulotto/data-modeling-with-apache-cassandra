from .base import DatabaseConnector
from cassandra.cluster import Cluster
import pandas as pd


class CassandraConnector(DatabaseConnector):
    """
    Connector class for interacting with Cassandra database.
    """

    def __init__(self, contact_points: list):
        """
        Initialize a new instance of CassandraConnector.

        Args:
            contact_points: A list of contact points for the Cassandra cluster.
        """
        self.contact_points = contact_points
        self.cluster = None
        self.session = None

    def connect(self):
        """
        Connect to the Cassandra database.
        """
        self.cluster = Cluster(contact_points=self.contact_points)
        self.session = self.cluster.connect()

    def disconnect(self):
        """
        Disconnect from the Cassandra database.
        """
        if self.cluster:
            self.cluster.shutdown()
        if self.session:
            self.session.shutdown()

    def execute_query(self, query: str):
        """
        Execute a query on the Cassandra database.

        Args:
            query: The query to execute.
        """
        return self.session.execute(query)

    def set_keyspace(self, keyspace: str):
        """
        Set the keyspace for the Cassandra session.

        Args:
            keyspace: The name of the keyspace to set.
        """
        self.session.set_keyspace(keyspace)

    def print_query_result(self, query: str):
        """
        Execute a query on the Cassandra database and print the result.

        Args:
            query: The query to execute.
        """
        result = self.execute_query(query)
        for row in result:
            print(row)

    def query_to_dataframe(self, query: str) -> pd.DataFrame:
        """
        Convert the result of a query to a pandas DataFrame.

        Args:
            query: The query to execute.
            result_set: The result set of the query.

        Returns:
            pd.DataFrame: The result set as a pandas DataFrame.
        """
        result_set = self.execute_query(query)
        rows = list(result_set)
        df = pd.DataFrame(rows)
        return df
