import numpy as np
import matplotlib.pyplot as plt

"""
Objetivos da seção:
    - Entender o básico do NumPy
    - Entender como criar arrays
    - Fatiar arrays
    - Abrir e mostrar imagens com NumPy
"""

print("\n-------- Básico NumPy --------\n")

basic_array = [1,2,3]
print(f"Basic python list: {basic_array} / {type(basic_array)}")
print(f"Conversion to NumPy array: {np.array(basic_array)} / {type(np.array(basic_array))}")

print(f"\narray_example_9_manual = {[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}")
print(f"array_example_9_numpy = {np.arange(0, 10, 1)}")

print(f"\nBlank 2x1 matrix (array):\n {np.zeros(shape=(2))}")
print(f"Blank 2x2 matrix:\n {np.zeros(shape=(2,2))}")
print(f"Blank 2x2x2 matrix:\n {np.zeros(shape=(2,2,2))}")

print(f"\nRandom array: {np.random.randint(0, 100, 10)}")

array = np.arange(0,50)
matrix = array.reshape(5,10)
print(f"\nReshape array:\n {matrix}") #array de 50 elementos para matriz 5x10
print(f"Shape: {matrix.shape}")
print(f"Slicing: do décimo elemento para frente\n {array[10:]}")
print(f"Slicing: do décimo elemento para trás\n {array[:10]}")
print(f"Slicing: todos elementos da linha 1 da matriz\n {matrix[1,:]}")
print(f"Slicing: todos elementos da coluna 1 da matriz\n {matrix[:,1]}")
print(f"Slicing: todos elementos da linha 0 a 3, nas coluna 0 a 2 da matriz\n {matrix[0:3,0:2]}")

array = np.arange(0,3)
referencia = array
copia = array.copy()
print(f"\nOriginal: {array} / Endereço: {hex(id(array))}")
print(f"Referencia: {referencia} / Endereço: {hex(id(referencia))}") #endereço igual ao de cima por que só esta apontando para o endereço
print(f"Cópia: {copia} / Endereço: {hex(id(copia))}")

print("\n-------- O que é uma imagem? --------\n")
print("""
Cinza: Uma matriz bi-dimensional (height x width) de pixels, em que cada pixel armazena um valor de 0 até 255 (escuro -> claro)
Colorida: Uma matriz tri-dimensional (height x width x 3_color_channels), cada canal tem o valor variando de 0 a 255
""")

print("\n-------- Imagens e NumPy --------\n")