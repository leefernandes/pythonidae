from abc import ABC, abstractclassmethod

class HelloWorlder(ABC):
    @abstractclassmethod
    def hello(self, suffix: str) -> str:
        """suffix a hello."""
        pass

    @abstractclassmethod
    def world(self, prefix: str) -> str:
        """prefix a world."""
        pass
