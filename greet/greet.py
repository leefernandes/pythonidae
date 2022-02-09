"""
greet module
"""

from helloworld.helloworlder import HelloWorlder


class Greet:
    """
    greet the world
    """

    __helloworlder: HelloWorlder

    def __init__(self, helloworlder: HelloWorlder):
        self.__helloworlder = helloworlder

    def run(self, hello: str, world: str) -> None:
        """
        run some print statements
        """
        print(f"a: {self.__helloworlder.hello(world)}")
        print(f"b: {self.__helloworlder.world(hello)}")
