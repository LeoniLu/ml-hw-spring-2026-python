import numpy as np
from sklearn import neighbors

class kNN(object):
    def __init__(self):
        self.N = 0
        self.k = 0
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

    def input_data(self, prompt: str):
        user_input = input(prompt).strip()
        try:
            x = float(user_input)
            return x
        except ValueError:
            print("Invalid input, please enter a real number!")
            return self.input_data(prompt)

    def load_data(self, x, y):
        self.dx = x
        self.dy = y


def main():
    knn = kNN()
    knn.N = knn.input_int("Please enter number of data points in total (positive integer): ")
    knn.k = knn.input_int("Please enter number of neighbors (positive integer): ")
    if knn.k > knn.N:
        print(f"Error: k={knn.k} cannot be greater than N={knn.N}.")
        return
    data_x = np.zeros(knn.N)
    data_y = np.zeros(knn.N)
    knn.load_data(data_x, data_y)
    for i in range(knn.N):
        knn.dx[i] = knn.input_data(f"Please enter x value for point {i+1}: ")
        knn.dy[i] = knn.input_data(f"Please enter y value for point {i+1}: ")
    print(f"N={knn.N}, k={knn.k}, {knn.dx}, {knn.dy}")
    print(f"The variance of labels (y-values) is {np.var(knn.dy)}.")
    # define hyperparameters and train the model
    knn_model = neighbors.KNeighborsRegressor(n_neighbors=knn.k)
    knn_model.fit(knn.dx.reshape(-1,1), knn.dy)

    x_input = knn.input_data("Please enter an input value for k-NN prediction:")
    result = knn_model.predict([[x_input]])[0]
    print(f"The prediction is {result}.")

if __name__ == "__main__":
    main()