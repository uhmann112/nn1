import numpy as np

x= [1,2,3]
y= [4,5,6]

a= [3,4,7]
b= [5,1,1]


matrix1 = np.array([x,y])

matrix2= np.array([a,b])

output = np.dot(matrix1,matrix2.T)

print("dotproduct of thos matrices is:")
print(output)