from greet.greet import Greet
from helloworld.english import English
from helloworld.vietnamese import Vietnamese

def main():
    vietnamese = Vietnamese
    greetInVietnamese = Greet(vietnamese)
    greetInVietnamese.run()

    english = English
    greetInEnglish = Greet(english)
    greetInEnglish.run()

if __name__ == "__main__":
    main()
