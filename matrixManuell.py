import numpy as np

matrixA= [
    [1,2,3],
    [4,5,6]
]

matrixB = [
    [1,2],
    [3,4],
    [5,6]
]


def calculateMatrixDotProduct(A,B):
    result = [[]]
    for i in range(len(A)):
        for j in range(len(B)):
            valA =A[i][j]
            valB = B[j][i]

            prod = valA *valB
            result += prod
            
    return result

print(calculateMatrixDotProduct(matrixA,matrixB))


#falsche multiolikation und result muss auch der selbe
#  datentyp sein wie das result sein wird

