from .base import BaseTableManager
from typing import Dict, List, Any
from ..connectors.cassandra_db import CassandraConnector
from cassandra.query import BatchStatement
from cassandra.cluster import ResultSet
import pandas as pd


class CassandraTableManager(BaseTableManager):
    """
    Class for managing tables in Cassandra.
    """

    def __init__(self, connector: CassandraConnector, keyspace: str):
        """
        Initialize a new instance of CassandraTableManager.

        Args:
            connector (CassandraConnector): The Cassandra connector
                                            to use for database operations.
            keyspace (str): The keyspace to use for table operations.
        """

        super().__init__(connector)
        self.keyspace = keyspace

    def create_keyspace(self, replication_strategy: str = "SimpleStrategy",
                        replication_factor: int = 1) -> None:
        """
        Create a keyspace in the Cassandra database.

        Args:
            replication_strategy (str): The replication strategy to use
                                        (default is "SimpleStrategy").
            replication_factor (int): The replication factor
                                        to use (default is 1).
        """
        query = f"CREATE KEYSPACE IF NOT EXISTS {self.keyspace} " \
                f"WITH REPLICATION = {{ 'class' : '{replication_strategy}', " \
                f"'replication_factor' : {replication_factor} }}"
        self.connector.execute_query(query)

    def set_keyspace(self) -> None:
        """
        Set the keyspace for the Cassandra session.
        """
        self.connector.set_keyspace(self.keyspace)

    def create_table(self, table_name: str, columns: Dict[str, str],
                     partition_key: List[str], clustering_key: List[str]
                     ) -> None:
        """
        Create a table in Cassandra.

        Args:
            table_name: The name of the table to create.
            columns: A dictionary of column names and their data types.
                     Key: The column name.
                     Value: The data type of the column.
            partition_key List[str]:
                    List of primary key columns
            clustering_key List[str]:
                    List of clustering key columns

        Returns:
            None.
        """
        column_defs = ', '.join(
            f"{name} {data_type}"
            for name, data_type in columns.items()
        )

        query = (
            f"CREATE TABLE IF NOT EXISTS {table_name} "
            f"({column_defs}, "
            f"{self._build_primary_key_str(partition_key, clustering_key)})"
        )

        self.connector.session.execute(query)

    def _build_primary_key_str(self, partition_key: List[str],
                               clustering_key: List[str]) -> str:
        """
        Build the primary key string.

        Args:
            partition_key List[str]:
                    List of primary key columns
            clustering_key List[str]:
                    List of clustering key columns

        Returns:
            str: The primary key string.
        """

        partition_key = f"{', '.join(partition_key)}"

        has_clustering_key = len(clustering_key) > 0
        if has_clustering_key:
            clustering_key = f"{', '.join(clustering_key)}"

        primary_key_str = "PRIMARY KEY (" + (
            f"({partition_key}), {clustering_key}" if has_clustering_key
            else partition_key
        ) + ")"

        return primary_key_str

    def insert_data(self, table_name: str, data: List[Dict[str, Any]]) -> None:
        """
        Insert data into the specified Cassandra table.

        Args:
            table_name: The name of the table to insert data into.
            data: A list of dictionaries containing the data to insert.
                Each dictionary represents a row of data.
                Key: The column name.
                Value: The corresponding data.

        Returns:
            None.
        """
        column_names = data[0].keys()
        placeholders = ', '.join(['?' for _ in column_names])
        prepared_query = (
            f"INSERT INTO {table_name} "
            f"({', '.join(column_names)}) "
            f"VALUES ({placeholders})"
        )

        prepared_statement = self.connector.session.prepare(prepared_query)

        batch = BatchStatement()

        batch_size = 100  # Adjust the batch size as per your requirements
        total_rows = len(data)

        for i in range(0, total_rows, batch_size):
            batch = BatchStatement()
            for row in data[i:i+batch_size]:
                values = list(row.values())
                batch.add(prepared_statement, values)

            self.connector.session.execute(batch)

    def drop_table(self, table_name: str) -> None:
        """
        Drop the specified Cassandra table.

        Args:
            table_name: The name of the table to drop.

        Returns:
            None.
        """
        query = f"DROP TABLE IF EXISTS {table_name}"
        self.connector.session.execute(query)

    def execute_query(self, query: str) -> ResultSet:
        """
        Execute a query on the Cassandra database.

        Args:
            query: The query to execute.

        Returns:
            The result set of the query.
        """
        return self.connector.session.execute(query)

    def print_query_result(self, result_set: ResultSet) -> None:
        """
        Print the result of a query.

        Args:
            result_set: The result set of the query.

        Returns:
            None.
        """
        for row in result_set:
            print(row)

    def query_to_dataframe(self, query: str) -> pd.DataFrame:
        """
        Convert the result of a query to a pandas DataFrame.

        Args:
            query: The query to execute.

        Returns:
            pd.DataFrame: The result set as a pandas DataFrame.
        """
        return self.connector.query_to_dataframe(query)
