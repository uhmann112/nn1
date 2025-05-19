import matplotlib.pyplot as plt
import numpy as np

# Beispiel-Daten
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 1, 3, 7])


colors = ['red' if val < 3 else 'green' for val in y]

plt.scatter(x, y, c=colors)
plt.title("Gefärbte Punkte nach Y-Wert")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
