"""
vietnamese
"""

from helloworld.helloworlder import HelloWorlder


class Vietnamese(HelloWorlder):
    """
    vietnamese helloworlder implementation
    """

    def hello(self, suffix: str) -> str:
        return f"xin chào {suffix}!"

    def world(self, prefix: str) -> str:
        return f"{prefix} thế giới!"
