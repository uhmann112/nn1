import numpy as np

inputs = [1,2,3]
weights = [3.5, -0.3,5]
bias = 3

############################################

output = np.dot(inputs,weights)+bias


print(f"the output is {output}")

#dies simuliert ein neuron das vom input layer oder anderen neuronen 3 inputs bekommt
#diese werden für einfachere rechnung in einen vector verwandelt unf mit np.dot mit den weights multipliziert