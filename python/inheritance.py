import sty
from sty import Style, RgbFg


class Vehicle:
    def __init__(self, name: str, color: tuple) -> None:
        self.name = name
        self.color = color

    def getname(self) -> str:
        return self.name

    def getcolor(self) -> tuple[int]:
        return self.color


class Car(Vehicle):
    def __init__(self, name: str, color: tuple) -> None:
        super().__init__(name=name, color=color)

    def __str__(self) -> str:
        sty.fg.custom = Style(RgbFg(self.color[0], self.color[1], self.color[2]))
        return sty.fg.custom + f"This is {self.name} ."


car1: Car = Car("kawin", (255, 234, 190))
print(car1)
print(car1.getname())
print(car1.getcolor())
