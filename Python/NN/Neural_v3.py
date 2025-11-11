import numpy as np


def normalize_data(data):
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    # Add a small constant to avoid division by zero
    return (data - mean) / (std + 1e-8)

def fill_missing_values(data, strategy='mean'):
    data = np.array(data)  # Convert list to NumPy array
    for i in range(data.shape[1]):
        if strategy == 'mean':
            data[:, i][np.isnan(data[:, i])] = np.mean(data[:, i][~np.isnan(data[:, i])])
        elif strategy == 'median':
            data[:, i][np.isnan(data[:, i])] = np.median(data[:, i][~np.isnan(data[:, i])])
    return data


class Neuron:
    def __init__(self, num_inputs, activation_name, learning_rate=0.01, error_func=None, l2_reg=0.01):
        self.l2_reg = l2_reg
        self.weights = np.random.uniform(low=-np.sqrt(6. / (num_inputs + 1)), 
                                         high=np.sqrt(6. / (num_inputs + 1)), 
                                         size=num_inputs)
        self.bias = np.random.uniform(low=-10, high=10)
        self.activation_name = activation_name
        self.learning_rate = learning_rate
        self.error_func = error_func
        self.activation_funcs = {
            'relu' : self.relu,
            'sigmoid': self.sigmoid,
            'hardlim': self.hardlim,
            'hardlims': self.hardlims,
            'compet' : self.compet,
            'tribase' : self.tribase,
            'poslin' : self.poslin,
            'purelin' : self.purelin,
            'radbas' : self.radbas,
            'satlin' : self.satlin,
            'satlins' : self.satlins,
            'softmax' : self.softmax,
            'tansig' : self.tansig,
            'logsig' : self.logsig
            #rest could be added here
        }
        # Add derivative functions for backpropagation
        self.derivative_funcs = {
            'relu' : self.relu_derivative,
            'sigmoid': self.sigmoid_derivative,
            'purelin' : self.purelin_derivative,
            # Add other derivative functions here
        }



    # Add derivative functions
    def relu_derivative(self, input_value):
        return np.where(input_value > 0, 1, 0)
    def sigmoid_derivative(self, input_value):
        sigmoid_value = self.sigmoid(input_value)
        return sigmoid_value * (1 - sigmoid_value)
    def purelin_derivative(self, input_value):
        return 1



    def relu(self, input_value):
        return np.maximum(0, input_value)
    def sigmoid(self, input_value):
        # Clip input_value to prevent overflow
        input_value = np.clip(input_value, -500, 500)
        return 1 / (1 + np.exp(-input_value))
    def compet(self, input_vector):
        # Assuming input_vector is a numpy array
        max_index = np.argmax(input_vector)
        output_vector = np.zeros_like(input_vector)
        output_vector[max_index] = 1
        return output_vector
    # Hard limit activation function
    def hardlim(self ,input_value):
        return 1 if input_value >= 0 else 0
    # Hard limits activation function
    def hardlims(self , input_value):
        return 1 if input_value > 0 else -1 if input_value < 0 else 0
    # Tri-base activation function (assuming it's a triangular basis function)
    def tribase(self ,input_value):
        return max(1 - abs(input_value), 0)
    # Positive linear activation function
    def poslin(self, input_value):
        return np.maximum(0, input_value)
    # Pure linear activation function
    def purelin(self, input_value):
        return input_value
    # Radial basis activation function
    def radbas(self ,input_value):
        return np.exp(-input_value**2)
    # Saturating linear activation function
    def satlin(self, input_value):
        return np.minimum(np.maximum(input_value, 0), 1)
    # Saturating linear activation function (symmetric)
    def satlins(self, input_value):
        return np.minimum(np.maximum(input_value, -1), 1)
    # Softmax activation function
    def softmax(self, input_vector):
        e_x = np.exp(input_vector - np.max(input_vector, axis=0, keepdims=True))
        return e_x / e_x.sum(axis=0, keepdims=True)
    # Hyperbolic tangent sigmoid activation function
    def tansig(self, input_value):
        return np.tanh(input_value)
    # Logistic sigmoid activation function
    def logsig(self ,input_value):
        return 1 / (1 + np.exp(-input_value))



    def activate(self, inputs):
        activation = np.dot(inputs, self.weights) + self.bias
        return self.activation_funcs[self.activation_name](activation)
    

    
    def calculate_error(self, output, target):
        l2_loss = 0.5 * self.l2_reg * np.sum(np.square(self.weights))
        return self.error_func(output, target) + l2_loss
        


    def clip_gradients(self, gradients, max_value=1.0):
        # Clip gradients to prevent exploding gradients
        return np.clip(gradients, -max_value, max_value)



    def update_weights_and_bias(self, inputs, output, target, derivative):
        error_derivative = 2 * (output - target) * derivative
        weights_gradient = error_derivative * inputs
        weights_gradient = self.clip_gradients(weights_gradient)
        self.weights -= self.learning_rate * (weights_gradient + self.l2_reg * self.weights)
        self.bias -= self.learning_rate * error_derivative





class NeuralNetwork:
    def __init__(self, num_inputs, neurons_per_layer, activation_names, err_formula_name, learning_rate=0.01, l2_reg=0.01):
        self.learning_rate = learning_rate
        self.error_funcs = {
            'mse': lambda output, target: (output - target) ** 2,
            'cross_entropy': lambda output, target: -(target * np.log(output) + (1 - target) * np.log(1 - output)),
            # Add other error functions here
        }
        self.err_formula = self.error_funcs[err_formula_name]

        self.layers = []
        for i, num_neurons in enumerate(neurons_per_layer):
            if i == 0:
                layer_inputs = num_inputs
            else:
                layer_inputs = neurons_per_layer[i-1]
            layer = [Neuron(layer_inputs, activation_names[i], learning_rate=self.learning_rate, error_func=self.err_formula, l2_reg=l2_reg) for _ in range(num_neurons)]
            self.layers.append(layer)




    def forward(self, inputs):
        activations = []
        for layer in self.layers:
            inputs = np.array([neuron.activate(inputs) for neuron in layer]).T
            activations.append(inputs)
        return activations
    


    def train(self, X, y, epochs, batch_size=32):
        num_batches = len(X) // batch_size
        for epoch in range(epochs):
            for batch in range(num_batches):
                batch_X = X[batch * batch_size:(batch + 1) * batch_size]
                batch_y = y[batch * batch_size:(batch + 1) * batch_size]
                total_error = 0
                for inputs, target in zip(batch_X, batch_y):
                    # Forward pass
                    activations = self.forward(inputs)
                    # Initialize next_layer_error for the output layer
                    next_layer_error = 2 * (activations[-1] - target)
                    for i, layer in reversed(list(enumerate(self.layers))):
                        layer_error = []
                        for j, neuron in enumerate(layer):
                            if i == len(self.layers) - 1:
                                # Output layer
                                error = neuron.calculate_error(activations[i][j], target[j])
                            else:
                                # Hidden layers
                                error = np.dot(next_layer_error, [neuron.weights for neuron in self.layers[i+1]])
                            derivative = neuron.derivative_funcsneuron.activation_name
                            neuron.update_weights_and_bias(activations[i-1] if i > 0 else inputs, activations[i][j], error, derivative)
                            layer_error.append(error)
                        next_layer_error = np.array(layer_error)
                    total_error += np.mean(np.square(next_layer_error))  # MSE
                if epoch % 100 == 0:
                    print(f"Epoch {epoch}, Error: {total_error}")
                    print(f"Network output: {self.forward(batch_X)[-1]}")
            self.learning_rate *= 0.99
        print(f"Final output of the network for the given input X after training: {self.forward(X)[-1]}")

    def fit(self, X):
        return self.forward(X)


    
    def print_network_data(self, layer_number=None):
        if layer_number is not None:
            # Print data for the specified layer
            layer = self.layers[layer_number - 1]
            print(f"Layer {layer_number}:")
            for j, neuron in enumerate(layer):
                print(f"  Neuron {j+1}:")
                print(f"    Weights: {neuron.weights}")
                print(f"    Bias: {neuron.bias}")
        else:
            # Print data for all layers
            for i, layer in enumerate(self.layers):
                print(f"Layer {i+1}:")
                for j, neuron in enumerate(layer):
                    print(f"  Neuron {j+1}:")
                    print(f"    Weights: {neuron.weights}")
                    print(f"    Bias: {neuron.bias}")
                print("\n")


num_inputs = 3
neurons_per_layer = [3, 4, 5, 4 , 3]
activation_names = ['purelin', 'purelin', 'purelin', 'purelin', 'purelin']  
err_formula_name = 'mse'
epochs = 100
X = [[2, 3, 4]] 
labels = [[4, 9, 16]] 
X1 = [[7,8,15]]

X_normalized = normalize_data(X)
labels_filled = fill_missing_values(labels)

network = NeuralNetwork(num_inputs, neurons_per_layer, activation_names, err_formula_name)
network.train(X_normalized, labels_filled, epochs)
print(network.fit(X1))

network.print_network_data()