
from magazine import utils

class Product:
    def __init__(self, name):
        self.name = name
        utils.log_action(f"Utworzono produkt: {self.name}")