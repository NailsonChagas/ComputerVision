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

resized = cv2.resize(img_RGB, (0, 0), img_RGB, 0.5, 0.5) #diminuindo imagem em 50%
print(resized.shape)
plt.imshow(resized)
plt.show()

print("\n--------- Girar Imagens ---------\n")
new = cv2.flip(img_RGB, 0) #inverte horizontalmente
plt.imshow(new)
plt.show()

new = cv2.flip(img_RGB, 1) #inverte verticalmente
plt.imshow(new)
plt.show()

new = cv2.flip(img_RGB, -1) #inverte nos dois eixos
plt.imshow(new)
plt.show()

print("\n--------- Salvar Imagens ---------\n")
img_BGR = cv2.cvtColor(new, cv2.COLOR_RGB2BGR)
cv2.imwrite('nova.jpg', img_BGR)

print("\n--------- Mostrar Imagens com OpenCV ---------\n")
while True:
    cv2.imshow('PUPPY', img_BGR)
    key = cv2.waitKey(10) #recebe a tecla clicada após 10ms
    if key != -1: print(key)
    if cv2.getWindowProperty("PUPPY", cv2.WND_PROP_VISIBLE) < 1:
            break
cv2.destroyAllWindows()

print("\n--------- Desenhando textos e poligonos na imagem ---------\n")
blank_img = np.zeros(shape=(500,500,3), dtype=np.int16)

cv2.rectangle(
    blank_img, 
    pt1=(250, 200), # top left corner 
    pt2=(350, 300), # bottom right corner
    color=(0,255,0), thickness=4
)
cv2.circle(blank_img, center=(250, 250), radius=30, color=(255,0,0), thickness=2)
cv2.circle(blank_img, center=(250, 250), radius=10, color=(255,0,0), thickness=-1)
cv2.line(blank_img, pt1=(0,0), pt2=(500,500), color=(0,0,255))
cv2.line(blank_img, pt1=(0,500), pt2=(500,0), color=(0,0,255), thickness=2)

cv2.putText(
    blank_img,
    text="TESTE",
    org=(10, 475),
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=3,
    thickness=2,
    color=(255,255,255)
)

plt.imshow(blank_img)
plt.show()

print("\n--------- Desenhando poligono customizado ---------\n")
blank_img = np.zeros(shape=(512,512,3), dtype=np.int32)

vertices = np.array(
    [
        [100,300], 
        [200,200], 
        [400,300], 
        [200, 400]
    ], 
    dtype=np.int32
)

pontos = vertices.reshape((-1,1,2))

cv2.polylines(
    blank_img, 
    pts = [pontos], 
    isClosed=True, 
    color=(255,255,0), 
    thickness=5
)

plt.imshow(blank_img)
plt.show()