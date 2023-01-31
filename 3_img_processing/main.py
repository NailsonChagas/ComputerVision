import matplotlib.pyplot as plt
import numpy as np
import cv2

print("""
--------- Processamento de Imagens ---------\n
Neste módulo será aprendido:
- Operações de processamento de imagens
- Execução de operações como:
    * Smoothing
    * Blurring
    * Operações Morfológicas
- Obter propriedades como histogramas e color space
""")

print("""
--------- Mapeamentos de cor ---------\n
- RGB: Red Green Blue
- RGBA: Red Green Blue Alpha
- HSV: Hue Saturation Value
- HSL: Hue Saturation Lightness
""")

print("--------- Convertendo Mapeamentos de cor ---------\n")
img_BGR = cv2.imread("./dog.jpg")
img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)
print(img_RGB.shape)
plt.imshow(img_RGB)
plt.show()

img_HSV = cv2.cvtColor(img_RGB, cv2.COLOR_RGB2HSV)
print(img_HSV.shape)
plt.imshow(img_HSV)
plt.show()

print("\n--------- Blending and Pasting: Combinando Imagens ---------")
print("""
- Blending: feito através da função addWeighted, que pega as 
imagens e as combina. Blend é feito seguindo a formula: 
    * new_pixel = (alpha x pixel_1) + (beta x pixel_2) + gamma
""")
DOG1 = img_RGB.copy()
DOG2 = cv2.flip(DOG1, 1)

blended = cv2.addWeighted(DOG1, 0.5, DOG2, 0.5, 0)
plt.imshow(blended)
plt.show()

print("""
--------- Blending and Pasting - Masks ---------\n
Como substituir apenas uma parte da imagem?  
Usando uma mascara, pesquisar melhor como fazer
""")