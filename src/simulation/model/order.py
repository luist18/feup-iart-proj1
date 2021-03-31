from simulation.model.place import Place


class Order(Place):

    id = 0

    def __init__(self, location, product_types):
        super().__init__(location)
        self.id = Order.id

        Order.id += 1

        self.product_types = product_types

    def is_completed(self):
        return len(self.product_types) == 0

    def remove(self, product_type):
        self.product_types.remove(product_type)

    def __str__(self):
        return f'o{self.id} {self.product_types} at {self.location}'

    def __repr__(self):
        return self.__str__()
