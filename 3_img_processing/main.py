import matplotlib.pyplot as plt
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
plt.imshow(img_RGB)
plt.show()

img_HSV = cv2.cvtColor(img_RGB, cv2.COLOR_RGB2HSV)
plt.imshow(img_HSV)
plt.show()