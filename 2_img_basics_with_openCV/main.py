import matplotlib.pyplot as plt
import numpy as np
import cv2

"""
Objetivos da seção:
    - Começar a entender o uso do OpenCV
    - Abrir imagens e desenhar em cima delas
"""

print("""
\n--------- OpenCV ---------\n
OpenCV: Open Source Computer Vision
Programada em: C++
É uma biblioteca focada principalmente em visão computacional em tempo real
""")

print("\n--------- Lendo imagens com OpenCV ---------\n")
img_BGR = cv2.imread('./puppy.jpg') 
print(type(img_BGR), img_BGR.shape)

plt.imshow(img_BGR)
plt.show()

"""
A imagem é diferente da original devido a difereças entre 
como o matplotlib e opencv lidam com a ordem dos canais de cores 
Matplot -> RBG
OpenCV -> BGR
"""

img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)
print(type(img_RGB), img_RGB.shape)
plt.imshow(img_RGB)
plt.show()

img_gray = cv2.imread('./puppy.jpg', cv2.IMREAD_GRAYSCALE)
print(type(img_gray), img_gray.shape)
plt.imshow(img_gray, cmap='gray')
plt.show()

print("\n--------- Redimensionando Imagens ---------\n")
print(img_RGB.shape)

resized = cv2.resize(img_RGB, (1000, 400))
print(resized.shape)
plt.imshow(resized)
plt.show()
