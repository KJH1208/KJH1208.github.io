import numpy as np

class MLP:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.01):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate

        # Initialize weights and biases
        self.W1 = np.random.randn(self.input_size, self.hidden_size)
        self.b1 = np.zeros((1, self.hidden_size))
        self.W2 = np.random.randn(self.hidden_size, self.output_size)
        self.b2 = np.zeros((1, self.output_size))

    def relu(self, x):
        return np.maximum(0, x)

    def relu_derivative(self, x):
        return (x > 0).astype(float)

    def softmax(self, x):
        exp_x = np.exp(x - np.max(x))
        return exp_x / exp_x.sum(axis=1, keepdims=True)

    def forward(self, x):
        self.z1 = np.dot(x, self.W1) + self.b1
        self.a1 = self.relu(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.softmax(self.z2)
        return self.a2

    def backward(self, x, y, output):
        m = y.shape[0]
        
        delta2 = output - y
        dW2 = np.dot(self.a1.T, delta2) / m
        db2 = np.sum(delta2, axis=0, keepdims=True) / m
        
        delta1 = np.dot(delta2, self.W2.T) * self.relu_derivative(self.z1)
        dW1 = np.dot(x.T, delta1) / m
        db1 = np.sum(delta1, axis=0, keepdims=True) / m

        self.W2 -= self.learning_rate * dW2
        self.b2 -= self.learning_rate * db2
        self.W1 -= self.learning_rate * dW1
        self.b1 -= self.learning_rate * db1

    def compute_loss(self, y, output):
        m = y.shape[0]
        log_likelihood = -np.log(output[range(m), y.argmax(axis=1)])
        loss = np.sum(log_likelihood) / m
        return loss

    def fit(self, X, y, epochs=100, batch_size=32, early_stopping=False, patience=5, validation_data=None):
        best_loss = float('inf')
        patience_counter = 0
        
        X_val, y_val = validation_data if validation_data else (None, None)
        
        for epoch in range(epochs):
            permutation = np.random.permutation(X.shape[0])
            X_shuffled = X[permutation]
            y_shuffled = y[permutation]
            
            for i in range(0, X.shape[0], batch_size):
                X_batch = X_shuffled[i:i+batch_size]
                y_batch = y_shuffled[i:i+batch_size]
                
                output = self.forward(X_batch)
                self.backward(X_batch, y_batch, output)
            
            if validation_data:
                val_output = self.forward(X_val)
                val_loss = self.compute_loss(y_val, val_output)
                print(f'Epoch {epoch+1}, Validation Loss: {val_loss}')
                
                if early_stopping:
                    if val_loss < best_loss:
                        best_loss = val_loss
                        patience_counter = 0
                    else:
                        patience_counter += 1
                    if patience_counter >= patience:
                        print("Early stopping")
                        break
            else:
                print(f'Epoch {epoch+1}, Loss: {self.compute_loss(y, self.forward(X))}')

    def predict(self, X):
        output = self.forward(X)
        return np.argmax(output, axis=1)

if __name__ == "__main__":
    # Test the MLP with dummy data
    input_size = 784  # Example for MNIST
    hidden_size = 128
    output_size = 10
    X_dummy = np.random.randn(100, input_size)
    y_dummy = np.eye(output_size)[np.random.choice(output_size, 100)]
    
    mlp = MLP(input_size, hidden_size, output_size)
    mlp.fit(X_dummy, y_dummy, epochs=10, batch_size=32)
    print(mlp.predict(X_dummy))
