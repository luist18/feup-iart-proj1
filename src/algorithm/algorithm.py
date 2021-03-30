from abc import ABC, abstractmethod
from timeit import default_timer as timer


class Algorithm(ABC):

    def __init__(self, simulation, max_time=None, max_iterations=None, max_improveless_iterations=20):
        self.simulation = simulation

        self.starting_time = timer()
        self.iterations = 0
        self.improveless_iterations = 0

        self.max_time = max_time
        self.max_iterations = max_iterations
        self.max_improveless_iterations = max_improveless_iterations

    @abstractmethod
    def run(self):
        pass

    def random_solution(self):
        orders = self.simulation.orders.copy()

        orders.sort(key=lambda order: self.simulation.order_weight(order))
        return ["a", "b", "c"]

    def evaluate(self, solution):
        # TODO
        return 10

    def stop(self):
        """Verifies if the algorithm must stop.

        ...
        Returns:
            boolean: True if the algorithm must stop, false otherwise
        """
        return self.max_time is not None and timer() - self.starting_time >= self.max_time \
            or self.max_iterations is not None and self.iterations >= self.max_iterations \
            or self.max_improveless_iterations <= self.improveless_iterations