import numpy as np


class Neuron:
    def __init__(self, num_inputs):
        self.weights = np.random.rand(num_inputs)  # Initialize random weights
        self.bias = np.random.rand()  # Initialize random bias
        self.learning_rate = 0.1  # Learning rate
        self.error = 0.0  # Initialize error

    def activate(self, inputs):
        # Perform summation of inputs weighted by weights and add bias
        activation = np.dot(inputs, self.weights) + self.bias
        output = self.sigmoid(activation)
        self.error = (output - 1) ** 2  # Mean squared error
        return output

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def gradient_descent(self, inputs, label):
        # Compute gradients for weights and bias using a single step
        activation = np.dot(inputs, self.weights) + self.bias
        output = self.sigmoid(activation)
        # Derivative of the error function
        error_derivative = 2 * (output - label)
        # Derivative of the sigmoid function
        sigmoid_derivative = output * (1 - output)
        weights_gradient = inputs * error_derivative * sigmoid_derivative
        bias_gradient = error_derivative * sigmoid_derivative

        # Update weights and bias
        self.weights -= self.learning_rate * weights_gradient
        self.bias -= self.learning_rate * bias_gradient


# ایجاد یک نرون با دو وزن و یک بایاس
neuron = Neuron(2)
X = np.array([[0.5, 0.3], [0.2, 0.7], [0.9, 0.1]])  # Features
labels = np.array([1, 0, 1])  # Corresponding labels

for i in range(len(X)):
    output = neuron.activate(X[i])
    neuron.gradient_descent(X[i], labels[i])

print("Weights after training:", neuron.weights)
print("Bias after training:", neuron.bias)
print("Output: ", output)
