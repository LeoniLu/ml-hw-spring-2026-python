#!python3

from collections import defaultdict
from collections.abc import Callable

class InputFinder(object):

    def __init__(self):
        self.input = defaultdict(lambda : -1)
        self.N = 0

    def input_int(self, prompt: str, validator: Callable[[int], bool]) -> int:
        user_input = input(prompt).strip()
        try:
            n = int(user_input)
            if validator(n):
                return n
            else:
                print("Invalid input, please enter an positive integer!")
        except ValueError:
            print("Invalid input, please enter an integer!")
        return self.input_int(prompt, validator)

    def set_n(self):
        valid = lambda n: n > 0
        self.N = self.input_int("Please enter a positive integer: ", valid)

        print(f"Success! You entered number {self.N}.")

    def take_value(self):
        for idx in range(self.N):
            prompt = f"Please enter int value for #{idx+1} element: "
            val = self.input_int(prompt, lambda x : True)
            self.input[val] = idx + 1

    def query(self):
        query = self.input_int("Please enter a value to query: ", lambda x : True)
        return self.input[query]

    def run(self):
        self.set_n()
        self.take_value()
        print(f"Answer: {self.query()}")


if __name__ == "__main__":
    finder = InputFinder()
    finder.run()


