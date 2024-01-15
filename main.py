class Vehicle:
    def __init__(self, model, year, confort):
        self.model = model
        self.year = year
        self.confort = confort

    def car(self):
        print(f"Model: {self.model}\nRok vyroby: {self.year}\nVybava: {self.confort}")

auto = Vehicle("Civic", 1985, "elegance")

auto.car()

