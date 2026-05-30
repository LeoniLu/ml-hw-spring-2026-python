import numpy as np
from sklearn.metrics import classification_report

class classification(object):
    def __init__(self):
        self.N = 0
        self.dx = None
        self.dy = None

    def input_int(self, prompt:str):
        user_input = input(prompt).strip()
        try:
            n = int(user_input)
            if n > 0:
                print(f"Success! You entered number {n}.")
                return n
            else:
                print("Invalid input, please enter a positive integer!")
                return self.input_int(prompt)
        except ValueError:
            print("Invalid input, please enter a positive integer!")
            return self.input_int(prompt)

    def input_data(self, prompt:str):
        user_input = input(prompt).strip()
        try:
            x = int(user_input)
            if x in [0,1]:
                return x
            else:
                print("Invalid input, please enter only 0 or 1!")
                return self.input_data(prompt)
        except ValueError:
            print("Invalid input, please enter only 0 or 1!")
            return self.input_data(prompt)

    def load_data(self, x, y):
        self.dx = x
        self.dy = y



def main():
    bin = classification()
    bin.N = bin.input_int("Please enter number of data points in total (positive integer): ")

    data_x = np.zeros(bin.N,dtype=int)
    data_y = np.zeros(bin.N,dtype=int)
    for i in range(bin.N):
        data_x[i] = bin.input_data(f"Please enter class for point {i+1}.x: ")
        data_y[i] = bin.input_data(f"Please enter class for point {i+1}.y: ")
    bin.load_data(data_x, data_y)
    print(f"N={bin.N}, x-ground_truth:{bin.dx}, y-predicted_class:{bin.dy}")

    # using zero_division=0 option to avoid invalid division
    report = classification_report(bin.dx, bin.dy, output_dict=True, zero_division=0)
    precision = report["1"]["precision"]
    recall = report["1"]["recall"]
    print(f"precision: {precision:0.2f}")
    print(f"recall: {recall:0.2f}")

if __name__ == "__main__":
    main()