import numpy as np
import os


def clrscr():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


class NeuralNetwork:
    def __init__(self, layer_sizes):
        # Extract layer sizes
        input_size, *hidden_sizes, output_size = layer_sizes

        # Initialize random weights and biases for the layers
        self.weights_input_hidden = np.random.rand(input_size, hidden_sizes[0])
        self.bias_hidden = np.random.rand(hidden_sizes[0])

        self.weights_hidden_output = np.random.rand(
            hidden_sizes[-1], output_size)
        self.bias_output = np.random.rand(output_size)

        self.learning_rate = 0.1

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, inputs):
        # Calculate hidden layer activations
        hidden_activation = np.dot(
            inputs, self.weights_input_hidden) + self.bias_hidden
        hidden_output = self.sigmoid(hidden_activation)

        # Calculate output layer activations
        output_activation = np.dot(
            hidden_output, self.weights_hidden_output) + self.bias_output
        output = self.sigmoid(output_activation)

        return output

    def train(self, inputs, labels):
        # Forward pass
        output = self.forward(inputs)

        # Compute gradients for output layer
        output_error = 2 * (output - labels) * output * (1 - output)
        hidden_output = self.sigmoid(
            np.dot(inputs, self.weights_input_hidden) + self.bias_hidden)
        weights_hidden_output_gradient = np.outer(hidden_output, output_error)
        bias_output_gradient = output_error

        # Update weights and biases
        self.weights_hidden_output -= self.learning_rate * weights_hidden_output_gradient
        self.bias_output -= self.learning_rate * bias_output_gradient

        # Compute gradients for hidden layer
        hidden_error = np.dot(
            output_error, self.weights_hidden_output.T) * hidden_output * (1 - hidden_output)
        weights_input_hidden_gradient = np.outer(inputs, hidden_error)
        bias_hidden_gradient = hidden_error

        # Update weights and biases
        self.weights_input_hidden -= self.learning_rate * weights_input_hidden_gradient
        self.bias_hidden -= self.learning_rate * bias_hidden_gradient


clrscr()
# Get user input for layer sizes
try:
    input_size = int(input("Enter the number of input neurons: "))
    hidden_size = int(
        input("Enter the number of neurons in the hidden layer: "))
    output_size = int(input("Enter the number of output neurons: "))
except ValueError:
    print("Invalid input. Please enter valid integer values.")

# Create a neural network with user-specified layer sizes
nn = NeuralNetwork(layer_sizes=[input_size, hidden_size, output_size])

# Training data (you can customize this)
X = np.array([[0.5, 0.3], [0.2, 0.7], [0.9, 0.1]])
labels = np.array([1, 0, 1])

# Train the network
for i in range(len(X)):
    nn.train(X[i], labels[i])

# Print trained weights and biases
print("\nWeights after training (input-hidden):", nn.weights_input_hidden)
print("\nBias after training (hidden):", nn.bias_hidden)
print("\nWeights after training (hidden-output):", nn.weights_hidden_output)
print("\nBias after training (output):", nn.bias_output, "\n")
