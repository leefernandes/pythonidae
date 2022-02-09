from greet.greet import Greet
from helloworld.english import English
from helloworld.vietnamese import Vietnamese

def main():
    vietnamese = Vietnamese
    greetInVietnamese = Greet(vietnamese)
    greetInVietnamese.run('🙂 xin chào', 'thế giới 🙂')

    english = English
    greetInEnglish = Greet(english)
    greetInEnglish.run('😈 hello', 'world 😈')

if __name__ == "__main__":
    main()
