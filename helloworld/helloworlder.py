"""
helloworlder
"""

from abc import ABC, abstractmethod


class HelloWorlder(ABC):
    """
    helloworlder interface
    """

    @abstractmethod
    def hello(self, suffix: str) -> str:
        """
        This abstract method should return a suffixed string:
        Returns:
            str: A string
        """
        raise NotImplementedError

    @abstractmethod
    def world(self, prefix: str) -> str:
        """
        This abstract method should return a prefixed string:
        Returns:
            str: A string
        """
        raise NotImplementedError
