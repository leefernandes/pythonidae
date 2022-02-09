from helloworld.helloworlder import HelloWorlder

class English(HelloWorlder):
  @classmethod
  def hello(self, suffix: str) -> str:
    return f"hello {suffix}!"

  @classmethod
  def world(self, prefix: str) -> str:
    return f"{prefix} world!"
