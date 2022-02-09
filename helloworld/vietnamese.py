from helloworld.helloworlder import HelloWorlder

class Vietnamese(HelloWorlder):
  @classmethod
  def hello(self, suffix: str) -> str:
    return f"xin chào {suffix}!"

  @classmethod
  def world(self, prefix: str) -> str:
    return f"{prefix} thế giới!"
