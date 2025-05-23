import numpy as np

inputs = [1,2,3,4,]

weights = [
    [0.25, -0.13, 0.40, 0.05],
    [-0.78, 0.22, 0.91, -0.33],
    [0.14, -0.56, 0.73, 0.18],
    [-0.45, 0.67, -0.29, 0.32]
]

biases = [2,-3,-0.3,2]

################################BERECHNUNG#################################

def sigmoid(x):
      return 1 / (1 + np.exp(-x))




output = []

for i in range(len(weights)):
    res = np.dot(inputs,weights[i])+biases[i]
    output.append(res)


output = [sigmoid(x) for x in output]
output= [float(item)for item in output]

print("")

for index in range(len(output)):
     print(f"       {output[index]}")

print("")






########################## YAPPING ZONE ###############################

# es gibt im layer davor 4 neurons, das heist der input ist ein vector aus 4 daten
# die neuronen haben alle ein eigenes weight set das mal 4 dh es iszt eine 4x 4 matrix