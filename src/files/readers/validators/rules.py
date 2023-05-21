from src.files.readers.validators.base import ValidationRule


class NotNullOrEmptyRule(ValidationRule):
    """
    Validation rule that checks if a value is not null or empty.
    """

    @staticmethod
    def is_valid(value):
        """
        Validate the value.

        :param value: The value to validate.
        :return: True if the value is not null or empty, False otherwise.
        """
        return value is not None and str(value).strip() != ""

    @staticmethod
    def error_message():
        """
        Get the error message associated with the validation rule.

        :return: The error message.
        """
        return "Value must not be null or empty."
