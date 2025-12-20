
from magazine import utils

class Order:
    def __init__(self, order_id):
        self.id = order_id
        utils.log_action(f"Złożono zamówienie nr: {self.id}")