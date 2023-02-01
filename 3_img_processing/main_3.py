import matplotlib.pyplot as plt
import numpy as np
import cv2

print("""
--------- Histograma de imagem ---------\n
- representação visual da distribuição de uma caracteristica continua
- podemos mostrar a frequencia em que valores de cores aparecem
""")

img_BGR = cv2.imread("./dog.jpg")
img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)
print(img_RGB.shape)
plt.imshow(img_RGB)
plt.show()

hist_red = cv2.calcHist([img_RGB], channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.plot(hist_red)
plt.show()

hist_green = cv2.calcHist([img_RGB], channels=[1], mask=None, histSize=[256], ranges=[0,256])
plt.plot(hist_green)
plt.show()

hist_blue = cv2.calcHist([img_RGB], channels=[2], mask=None, histSize=[256], ranges=[0,256])
plt.plot(hist_blue)
plt.show()

for i,color in enumerate(('r', 'g', 'b')):
    hist = cv2.calcHist([img_RGB], channels=[i], mask=None, histSize=[256], ranges=[0,256])
    plt.plot(hist, color=color)
plt.show()