class Glassware:
    def __init__(self, material):
        self.material = material


class Beaker(Glassware):
    def __init__(self, material, capacity):
        super().__init__(material)
        self.capacity = capacity


class Tray:
    def __init__(self):
        self.beakers = [
            Beaker("Glass", 100),
            Beaker("Glass", 150),
            Beaker("Glass", 200),
            Beaker("Glass", 250),
            Beaker("Glass", 300),
        ]


tray = Tray()

print("Number of beakers:", len(tray.beakers))
print("First beaker:", tray.beakers[0].capacity, "mL")

del tray
