def quack(thing):
    thing.quack()


class Duck:
    def quack(self): print("Quack!")


class Person:
    def quack(self): print("I can imitate a duck!")


quack(Duck())  # Quack!
quack(Person())  # I can imitate a duck!


class IdGenerator:
    def generate(self): print("Random Id")


def quack(thing):
    if hasattr(thing, "quack"):
        thing.quack()
    else:
        print("I can't quack :(")


quack(IdGenerator())
