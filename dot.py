
import numpy as np


x= [1,2,3]
y= [4,5,6]

x2= np.array([1,2,3])
y2= np.array([4,5,6])

def CalculateDotProduct(x,y):
    if len(x) == len(y):
        result = 0
        for i in range(len(x)):
            result += x[i-1]*y[i-1]
        return result
    

output =CalculateDotProduct(x,y)

dotproduct = np.dot(x2,y2)

print(f"the dot product is {output}")


print(f"the dot product with numpy  is {dotproduct}")

if output == dotproduct:
    print("succes!!!")


