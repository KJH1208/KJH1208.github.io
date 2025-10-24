import numpy as np
from sklearn.metrics import log_loss, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_openml

class LogisticRegressionSGD:
    def __init__(self, learning_rate=0.01, epochs=100, batch_size=32, patience=10, min_delta=1e-4):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.batch_size = batch_size
        self.patience = patience
        self.min_delta = min_delta

    def softmax(self, z):
        exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)

    def fit(self, X, y, X_val, y_val):
        self.W = np.random.randn(X.shape[1], y.shape[1])
        self.b = np.zeros((1, y.shape[1]))
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

                predictions = self.softmax(np.dot(X_mini, self.W) + self.b)
                error = predictions - y_mini

                gradient_W = np.dot(X_mini.T, error) / self.batch_size
                gradient_b = np.sum(error, axis=0, keepdims=True) / self.batch_size

                self.W -= self.learning_rate * gradient_W
                self.b -= self.learning_rate * gradient_b

            val_predictions = self.softmax(np.dot(X_val, self.W) + self.b)
            val_loss = log_loss(y_val, val_predictions)

            if val_loss < best_loss - self.min_delta:
                best_loss = val_loss
                epochs_no_improve = 0
            else:
                epochs_no_improve += 1

            if epochs_no_improve >= self.patience:
                print(f'Early stopping on epoch {epoch+1}')
                break

            train_acc = accuracy_score(np.argmax(y, axis=1), self.predict(X))
            val_acc = accuracy_score(np.argmax(y_val, axis=1), self.predict(X_val))
            print(f'Epoch {epoch + 1}/{self.epochs}, Validation Loss: {val_loss}, Training Accuracy: {train_acc}, Validation Accuracy: {val_acc}')

    def predict(self, X):
        probabilities = self.softmax(np.dot(X, self.W) + self.b)
        return np.argmax(probabilities, axis=1)

# MNIST 데이터셋 테스트
def test_mnist():
    mnist = fetch_openml('mnist_784', as_frame=False)
    X = mnist.data / 255.0
    y = mnist.target.astype(int)
    y = np.eye(10)[y]  # 원-핫 인코딩

    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

    model = LogisticRegressionSGD(learning_rate=0.01, epochs=100, batch_size=32, patience=10, min_delta=1e-4)
    model.fit(X_train, y_train, X_val, y_val)

    train_predictions = model.predict(X_train)
    val_predictions = model.predict(X_val)
    test_predictions = model.predict(X_test)

    print(f'Training Log Loss: {log_loss(y_train, model.softmax(np.dot(X_train, model.W) + model.b))}')
    print(f'Validation Log Loss: {log_loss(y_val, model.softmax(np.dot(X_val, model.W) + model.b))}')
    print(f'Test Log Loss: {log_loss(y_test, model.softmax(np.dot(X_test, model.W) + model.b))}')

    print(f'Training Accuracy: {accuracy_score(np.argmax(y_train, axis=1), train_predictions)}')
    print(f'Validation Accuracy: {accuracy_score(np.argmax(y_val, axis=1), val_predictions)}')
    print(f'Test Accuracy: {accuracy_score(np.argmax(y_test, axis=1), test_predictions)}')

# 사용 예시
test_mnist()
