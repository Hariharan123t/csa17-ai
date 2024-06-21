import numpy as np

class FeedforwardNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.1):
        # Initialize weights
        self.W1 = np.random.randn(input_size, hidden_size)
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size)
        self.b2 = np.zeros((1, output_size))
        self.learning_rate = learning_rate

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def sigmoid_derivative(self, z):
        return z * (1 - z)
    
    def feedforward(self, X):
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.sigmoid(self.z2)
        return self.a2
    
    def backpropagation(self, X, y, output):
        output_error = y - output
        output_delta = output_error * self.sigmoid_derivative(output)
        
        hidden_error = np.dot(output_delta, self.W2.T)
        hidden_delta = hidden_error * self.sigmoid_derivative(self.a1)
        
        self.W2 += self.learning_rate * np.dot(self.a1.T, output_delta)
        self.b2 += self.learning_rate * np.sum(output_delta, axis=0, keepdims=True)
        self.W1 += self.learning_rate * np.dot(X.T, hidden_delta)
        self.b1 += self.learning_rate * np.sum(hidden_delta, axis=0, keepdims=True)
    
    def train(self, X, y, epochs=10000):
        for _ in range(epochs):
            output = self.feedforward(X)
            self.backpropagation(X, y, output)
    
    def predict(self, X):
        output = self.feedforward(X)
        return np.round(output)

# Example usage:
if __name__ == "__main__":
    # Sample dataset: XOR function
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    # Create neural network
    nn = FeedforwardNeuralNetwork(input_size=2, hidden_size=2, output_size=1, learning_rate=0.1)
    
    # Train neural network
    nn.train(X, y, epochs=10000)
    
    # Predictions
    predictions = nn.predict(X)
    print("Predictions:\n", predictions)
