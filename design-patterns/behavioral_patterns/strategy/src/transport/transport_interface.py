from abc import ABC
from abc import abstractmethod


class Transport(ABC):
    """AN interface for each mood of transport"""

    @abstractmethod
    def operation(self, speed):
        """Each class will provide its own implementation using this function."""
        pass
