# Array indexing in NumPy
import numpy as np
print("---Indexación en Arreglos 1D (Unidimensional)-0120---")
n0120 = np.array([10, 20, 30, 40, 50])
print(n0120)
print(n0120[0])   
print(n0120[3])   
print(n0120[-1]) 
print(n0120[-2])  
print("---Indexación en Arreglos 2D (Bidimensional / Matriz)-0120---")
n0120 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(n0120)
print(n0120[0, 0])  
print(n0120[1, 2])   
print(n0120[-1, -1]) 
print(n0120[-2, -2]) 
print("---Indexación en Arreglos 3D (Tridimensional)-0120---")
# Arreglo 3D de forma 2x(2x3)
n0120 = np.array([
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])
print(n0120)
print(n0120[0, 0, 0]) 
print("Nicole Robles NC 0120")
