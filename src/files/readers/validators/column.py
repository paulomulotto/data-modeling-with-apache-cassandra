class ColumnValidator:
    """
    Class to validate columns of a DataFrame using specified rules.
    """

    def __init__(self, rules, dataframe):
        """
        Initialize a ColumnValidator instance with the specified rules and DataFrame.

        :param rules: A dictionary of column names and corresponding validation rules.
                      Each rule can be a single rule object or a list of rule objects.
        :param dataframe: The DataFrame to validate.
        :raises ValueError: If any column name in the rules dictionary is not found in the DataFrame.
        """
        self.rules = rules
        self._validate_column_names(dataframe)

    def _validate_column_names(self, dataframe):
        """
        Validate if all column names in the rules are present in the DataFrame.

        :param dataframe: The DataFrame to validate.
        :raises ValueError: If any column name in the rules dictionary is not found in the DataFrame.
        """
        dataframe_columns = set(dataframe.columns)
        invalid_columns = set(self.rules.keys()) - dataframe_columns
        if invalid_columns:
            raise ValueError(f"Invalid column name(s): {', '.join(invalid_columns)}")

    def _validate_column(self, column_name, column):
        """
        Validate a specific column based on the specified rules.

        :param column_name: The name of the column to validate.
        :param column: The column to validate.
        :return: True if the column passes all the validation rules, False otherwise.
        """
        rules = self.rules[column_name]

        if not isinstance(rules, list):
            rules = [rules]

        for rule in rules:
            if not rule.is_valid(column):
                return False

        return True

    def validate(self, dataframe):
        """
        Validate all columns of the given DataFrame based on the specified rules.

        :param dataframe: The DataFrame to validate.
        :return: A dictionary with column names as keys and boolean values indicating if the columns pass validation.
        """
        validation_results = {}

        for column_name in self.rules.keys():
            column = dataframe[column_name]
            validation_results[column_name] = self._validate_column(column_name, column)

        return validation_results
