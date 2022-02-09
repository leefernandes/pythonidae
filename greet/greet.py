from helloworld.helloworlder import HelloWorlder

class Greet:
  helloworlder: HelloWorlder = None

  def __init__(self, helloworlder: HelloWorlder):
    self.helloworlder = helloworlder

  def run(self):
    print(self.helloworlder.hello("world"))
    print(self.helloworlder.world("hello"))

