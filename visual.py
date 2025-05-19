import numpy as np
import matplotlib.pyplot as plt

# Init
inputVector = np.random.uniform(0, 5, size=2)
target = 0

weights = np.array([1.45, -0.66])
bias = 0.0
learningRate = 0.1

# Funktionen
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def makePrediction(inputVector, weights, bias):
    z = np.dot(inputVector, weights) + bias
    return sigmoid(z)

# Speicher für Visualisierung
errors = []
predictions = []
weight_history = []

# Trainingsloop
epochs = 50
for epoch in range(epochs):
    # Vorhersage
    prediction = makePrediction(inputVector, weights, bias)

    # Fehler
    error = np.square(prediction - target)
    errors.append(error)
    predictions.append(prediction)
    weight_history.append(weights.copy())

    # Gradienten berechnen
    dError_dPrediction = 2 * (prediction - target)
    dPrediction_dZ = prediction * (1 - prediction)
    dZ_dWeights = inputVector

    gradient = dError_dPrediction * dPrediction_dZ * dZ_dWeights

    # Update
    weights = weights - learningRate * gradient
    # Bias-Update (optional)
    db = dError_dPrediction * dPrediction_dZ * 1
    bias = bias - learningRate * db

# Ergebnis anzeigen
print(f"Final prediction: {prediction:.3f}")
print(f"Target: {target} => Final error: {error:.3f}")

# 📈 Visualisierung
plt.figure(figsize=(12, 5))

# Fehlerverlauf
plt.subplot(1, 2, 1)
plt.plot(errors, label='Fehler')
plt.xlabel('Epoche')
plt.ylabel('Fehler')
plt.title('Fehler über Zeit')
plt.legend()

# Gewichtsverlauf
plt.subplot(1, 2, 2)
weights_arr = np.array(weight_history)
plt.plot(weights_arr[:, 0], label='w1')
plt.plot(weights_arr[:, 1], label='w2')
plt.xlabel('Epoche')
plt.ylabel('Gewichtswert')
plt.title('Gewichte über Zeit')
plt.legend()

plt.tight_layout()
plt.show()
