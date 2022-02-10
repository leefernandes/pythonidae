"""
python playground
"""

from greet.greet import Greet
from helloworld.english import English
from helloworld.vietnamese import Vietnamese

from datetime import datetime
from pandas import Timestamp


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
    print("")
    timestamp()


def timestamp():
    ts = Timestamp(datetime.now())
    print(f"{ts.year}Q{ts.quarter}")


if __name__ == "__main__":
    main()
