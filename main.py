from greet.greet import Greet
from helloworld.vietnamese import Vietnamese

def main():
    vietnamese = Vietnamese
    greeting = Greet(vietnamese)
    greeting.run()

if __name__ == "__main__":
    main()
