import tensorflow as tf
import numpy as np
import os
import matplotlib.pyplot as plt

X = np.array([2,10,52,11,35,15,6,120,540,25])
Labels = np.array([7,23,107,25,73,33,15,243,1083,53])
test = np.array([167,20,1500,10000])
labels = np.array([337,43,3003,20003])

X = X.reshape(-1, 1)
Labels = Labels.reshape(-1, 1)
test = test.reshape(-1, 1)
labels = labels.reshape(-1, 1)

train_X = X[:int(len(X)*0.7)]
train_Labels = Labels[:int(len(Labels)*0.7)]
test_X = X[int(len(X)*0.7):]
test_Labels = Labels[int(len(Labels)*0.7):]

model = tf.keras.Sequential([
    tf.keras.layers.Dense(9, activation='relu'),
    tf.keras.layers.Dense(27, activation='relu'),
    tf.keras.layers.Dense(81, activation='relu'),
    tf.keras.layers.Dense(1)
])

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()

model.compile(optimizer='adam',
              loss=tf.keras.losses.MeanSquaredError(),
              metrics=['mse'])

history = model.fit(train_X, train_Labels, epochs=500, validation_data=(test_X, test_Labels))

plt.figure(figsize=(12, 6))
plt.title('Training and Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.show()

print("train :\n")
predictions = model.predict(X)
print(predictions)
print(Labels)
print("test :\n")
predictions = model.predict(test)
print(predictions)
print(labels)