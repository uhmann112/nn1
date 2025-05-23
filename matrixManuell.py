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


def calculateMatrixDotProduct(A, B):
    # Anzahl Zeilen von A und Spalten von B bestimmen
    rows_A = len(A)
    cols_B = len(B[0])
    cols_A = len(A[0])

    # Ergebnis-Matrix initialisieren
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Matrixmultiplikation durchführen
    for i in range(rows_A):        # Zeilen von A
        for j in range(cols_B):    # Spalten von B
            for k in range(cols_A):  # oder len(B), da A-Spalten = B-Zeilen
                result[i][j] += A[i][k] * B[k][j]
    
    return result


print(calculateMatrixDotProduct(matrixA, matrixB))
