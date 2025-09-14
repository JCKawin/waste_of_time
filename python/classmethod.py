class Car:
    total: int = 0

    def __init__(self, name: str, top_speed: str) -> None:
        self.top: int = top_speed
        self.brand: str = name
        Car.total += 1

    @classmethod
    def auto_speed(cls , Brand:str):
        database : dict[str,int] = {"Bmw":800 , "haxa":450, "jaguar":700}
        top_speed: int | None =database.get(Brand.lower())
        if top_speed:
            top_speed = top_speed
        else:
            top_speed = 200

        return cls(name=Brand , top_speed=top_speed )

    def __str__(self):
        return f"this is a {self.brand} with a top speed of {self.top}"


bmw: Car = Car("Bmw", 700)
jaguar: Car = Car.auto_speed("maruthi")

print(bmw)
print(jaguar)

