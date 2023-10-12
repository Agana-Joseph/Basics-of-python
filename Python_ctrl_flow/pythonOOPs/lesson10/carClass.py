class car:
    def __init__(self, manufacturer, color, year, type):
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        self.type = type

    def drive(self):
        print("Opening the the door")
        print("Turining on the engine")
        print("Vruuum...")
        print("Drive away")


toyota = car("Toyota", "Red", 2022, "suv")
toyota.drive()
Benz = car("Mecedec", "Blue", 2023, "EP")
Benz.drive()
Rang = car("RangRover", "White", 2023, "Velar")
Rang.drive()
