"""
python playground
"""

from greet.greet import Greet
from helloworld.english import English
from helloworld.vietnamese import Vietnamese


def main():
    """
    main
    """
    vietnamese = Vietnamese()
    greet_in_vietnamese = Greet(vietnamese)
    greet_in_vietnamese.run("🙂 xin chào", "thế giới 🙂")

    english = English()
    greet_in_english = Greet(english)
    greet_in_english.run("😈 hello", "world 😈")


if __name__ == "__main__":
    main()
