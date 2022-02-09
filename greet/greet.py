from helloworld.helloworlder import HelloWorlder

class Greet:
  __helloworlder: HelloWorlder = None

  def __init__(self, helloworlder: HelloWorlder):
    self.__helloworlder = helloworlder

  def run(self):
    print(f"a: {self.__helloworlder.hello('world')}")
    print(f"b: {self.__helloworlder.world('hello')}")

