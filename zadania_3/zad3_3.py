class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property at {self.address}, Area: {self.area}m², Rooms: {self.rooms}, Price: ${self.price}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House at {self.address}, Area: {self.area}m², Rooms: {self.rooms}, Price: ${self.price}, Plot: {self.plot}m²"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat at {self.address}, Area: {self.area}m², Rooms: {self.rooms}, Price: ${self.price}, Floor: {self.floor}"

house1 = House(120, 5, 300000, "Green St 10", 500)
flat1 = Flat(60, 3, 150000, "Blue St 5", 2)

print(house1)
print(flat1)
