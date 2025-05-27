from abc import abstractmethod, ABC


class Shape(ABC):
    @abstractmethod
    def draw(self) -> str:
        return "Default"


class Circle(Shape):
    def draw(self) -> str:
        return "Radius"


def print_shape(shape: Shape):
    print("Our shape is: " + shape.draw())


print_shape(Circle())

print(isinstance(Circle(), Shape))
print(issubclass(Circle, Shape))
