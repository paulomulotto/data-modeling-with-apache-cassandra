from abc import ABC, abstractmethod

class ValidationRule(ABC):
    """
    Abstract base class for validation rules.
    """

    @abstractmethod
    def is_valid(self, value):
        """
        Validate the value.

        :param value: The value to validate.
        :return: True if the value passes the validation rule, False otherwise.
        """
        pass

    @abstractmethod
    def error_message(self):
        """
        Get the error message associated with the validation rule.

        :return: The error message.
        """
        pass
