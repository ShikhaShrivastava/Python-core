class Bike:
    def __init__(self, name, model, colour, price):
        self.name = name
        self.model = model
        self.colour = colour
        self.price = price

    def get_bike_info(self):
        print(self.name, '/', self.model, '/', self.colour, '/', self.price)
