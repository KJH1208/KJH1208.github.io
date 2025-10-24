import numpy as np
import pickle
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes


class LinearRegressionSGD:
    def __init__(self, learning_rate=0.01, epochs=1000, batch_size=32, patience=10, min_delta=1e-4):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.batch_size = batch_size
        self.patience = patience
        self.min_delta = min_delta

    def fit(self, X, y, X_val, y_val):
        self.w = np.random.randn(X.shape[1])
        self.b = 0
        best_loss = float('inf')
        epochs_no_improve = 0

        for epoch in range(self.epochs):
            indices = np.arange(X.shape[0])
            np.random.shuffle(indices)
            X = X[indices]
            y = y[indices]

            for i in range(0, X.shape[0], self.batch_size):
                X_mini = X[i:i + self.batch_size]
                y_mini = y[i:i + self.batch_size]

                predictions = np.dot(X_mini, self.w) + self.b
                gradient_w = (2 / self.batch_size) * np.dot(X_mini.T, (predictions - y_mini))
                gradient_b = (2 / self.batch_size) * np.sum(predictions - y_mini)

                self.w -= self.learning_rate * gradient_w
                self.b -= self.learning_rate * gradient_b

            val_predictions = np.dot(X_val, self.w) + self.b
            val_loss = np.mean((val_predictions - y_val) ** 2)

            if val_loss < best_loss - self.min_delta:
                best_loss = val_loss
                epochs_no_improve = 0
            else:
                epochs_no_improve += 1

            if epochs_no_improve >= self.patience:
                print(f'Early stopping on epoch {epoch + 1}')
                break

            print(f'Epoch {epoch + 1}/{self.epochs}, Validation Loss: {val_loss}')

    def predict(self, X):
        return np.dot(X, self.w) + self.b


# 랜덤 데이터셋 로드 및 테스트
def test_random_dataset(filename):
    with open(filename, 'rb') as f:
        dataset = pickle.load(f)

    X_train = dataset['X_train']
    y_train = dataset['y_train']
    X_dev = dataset['X_dev']
    y_dev = dataset['y_dev']
    X_test = dataset['X_test']
    y_test = dataset['y_test']

    model = LinearRegressionSGD(learning_rate=0.01, epochs=1000, batch_size=32, patience=10, min_delta=1e-4)
    model.fit(X_train, y_train, X_dev, y_dev)

    train_predictions = model.predict(X_train)
    dev_predictions = model.predict(X_dev)
    test_predictions = model.predict(X_test)

    print(f'Training MSE: {mean_squared_error(y_train, train_predictions)}')
    print(f'Dev MSE: {mean_squared_error(y_dev, dev_predictions)}')
    print(f'Test MSE: {mean_squared_error(y_test, test_predictions)}')

    print(f'Training R^2: {r2_score(y_train, train_predictions)}')
    print(f'Dev R^2: {r2_score(y_dev, dev_predictions)}')
    print(f'Test R^2: {r2_score(y_test, test_predictions)}')


# 예시
test_random_dataset('myrandomdataset_1000.pkl')
test_random_dataset('myrandomdataset_10000.pkl')
test_random_dataset('myrandomdataset_100000.pkl')


# Scikit-learn 샘플 데이터 사용
def test_sklearn_diabetes():
    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegressionSGD(learning_rate=0.01, epochs=1000, batch_size=32, patience=10, min_delta=1e-4)
    model.fit(X_train, y_train, X_val, y_val)

    train_predictions = model.predict(X_train)
    val_predictions = model.predict(X_val)

    print(f'Training MSE: {mean_squared_error(y_train, train_predictions)}')
    print(f'Validation MSE: {mean_squared_error(y_val, val_predictions)}')

    print(f'Training R^2: {r2_score(y_train, train_predictions)}')
    print(f'Validation R^2: {r2_score(y_val, val_predictions)}')


#예시
test_sklearn_diabetes()
