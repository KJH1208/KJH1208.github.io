import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from MLP import MLP

# Load MNIST dataset
mnist = fetch_openml('mnist_784', version=1)
X = mnist.data / 255.0  # Normalize the data to [0, 1]
y = mnist.target.astype(int)

# One-hot encode the labels
encoder = OneHotEncoder(sparse=False)
y = encoder.fit_transform(y.reshape(-1, 1))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the MLP model
input_size = X_train.shape[1]
hidden_size = 128
output_size = y_train.shape[1]

mlp = MLP(input_size, hidden_size, output_size)
mlp.fit(X_train, y_train, epochs=50, batch_size=64, early_stopping=True, patience=5, validation_data=(X_test, y_test))

# Evaluate the model
y_pred = mlp.predict(X_test)
accuracy = np.mean(np.argmax(y_test, axis=1) == y_pred)
print(f'Test Accuracy: {accuracy * 100:.2f}%')
