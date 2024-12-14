import numpy as np

class LinearRegression:
    def __init__(self, lr=0.001, n_iters=1000) -> None:
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samps, n_feats = X.shape
        self.weights = np.zeros(n_feats)
        self.bias = 0

        for _ in range(self.n_iters):
            # y_pred = w*x + b
            y_pred = np.dot(X, self.weights) + self.bias

            ddw = (1/n_samps) * np.dot(2*X.T, (y_pred-y))
            ddb = (1/n_samps) * np.sum(2*(y_pred-y))

            self.weights = self.weights - self.lr * ddw
            self.bias = self.bias - self.lr * ddb

    def predict(self, X):
        y_pred = np.dot(X, self.weights) + self.bias
        return y_pred
