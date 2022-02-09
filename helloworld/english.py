"""
english
"""

from helloworld.helloworlder import HelloWorlder


class English(HelloWorlder):
    """
    english helloworlder implementation
    """

    def hello(self, suffix: str) -> str:
        return f"hello {suffix}!"

    def world(self, prefix: str) -> str:
        return f"{prefix} world!"
