
import numpy as np
import matplotlib.pyplot as pl




    inputVector = np.random.uniform(0, 5, size=2)

    target = 0

    weights = np.array([1.45, -0.66])
    bias = np.array([0.0])


    def sigmoid(x):
        return 1 / (1 + np.exp(-x))



    def makePrediction(inputVector,weights,bias):
        layer1 = np.dot(inputVector,weights)+bias
        layer2 = sigmoid(layer1)

        return layer2



    prediction = makePrediction(inputVector,weights,bias)
    error = np.square(prediction-target)



    print(f"the neuron predicted: {round(prediction,3)}")
    print(f"target: {target} ==> error: {round(error,3)}")




