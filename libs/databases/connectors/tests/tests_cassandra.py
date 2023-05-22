import unittest
from unittest.mock import Mock
from cassandra.cluster import Cluster
import pandas as pd
from libs.databases.connectors.cassandra_db import CassandraConnector


class TestCassandraConnector(unittest.TestCase):
    def setUp(self):
        # Create a mock Cluster object
        self.mock_cluster = Mock(spec=Cluster)

        # Create a mock Session object
        self.mock_session = self.mock_cluster.connect.return_value

        # Create an instance of CassandraConnector for testing
        self.connector = CassandraConnector(contact_points=['127.0.0.1'])

        # Set the mock objects as attributes of the connector
        self.connector.cluster = self.mock_cluster
        self.connector.session = self.mock_session

    def tearDown(self):
        # Reset the mock objects
        self.mock_cluster.reset_mock()
        self.mock_session.reset_mock()

    def test_connect(self):
        # Test the connect method
        self.connector.connect()

        # Assert that the Cluster is created
        self.mock_cluster.connect.assert_called_once_with()

    def test_disconnect(self):
        # Test the disconnect method
        self.connector.disconnect()

        # Assert that the Cluster and Session are shut down
        self.mock_cluster.shutdown.assert_called_once()
        self.mock_session.shutdown.assert_called_once()

    def test_execute_query(self):
        # Set up a mock result
        mock_result = Mock()
        self.mock_session.execute.return_value = mock_result

        # Test the execute_query method
        query = "SELECT * FROM table"
        result = self.connector.execute_query(query)

        # Assert that the query is executed on the Session
        self.mock_session.execute.assert_called_once_with(query)

        # Assert that the result is returned
        self.assertEqual(result, mock_result)

    def test_print_query_result(self):
        # Set up a mock result
        mock_result = [Mock(), Mock(), Mock()]
        self.mock_session.execute.return_value = mock_result

        # Test the print_query_result method
        query = "SELECT * FROM table"
        self.connector.print_query_result(query)

        # Assert that the query is executed on the Session
        self.mock_session.execute.assert_called_once_with(query)

    def test_set_keyspace(self):
        # Test the set_keyspace method
        keyspace = "mykeyspace"
        self.connector.set_keyspace(keyspace)

        # Assert that the keyspace is set on the Session
        self.mock_session.set_keyspace.assert_called_once_with(keyspace)

    def test_query_to_dataframe(self):
        # Set up a mock result set
        mock_result_set = [Mock(), Mock(), Mock()]
        self.mock_session.execute.return_value = mock_result_set

        # Test the query_to_dataframe method
        query = "SELECT * FROM table"
        df = self.connector.query_to_dataframe(query)

        # Assert that the query is executed on the Session
        self.mock_session.execute.assert_called_once_with(query)

        # Assert that the result set is converted to a DataFrame
        expected_df = pd.DataFrame(mock_result_set)
        pd.testing.assert_frame_equal(df, expected_df)


if __name__ == "__main__":
    unittest.main()
