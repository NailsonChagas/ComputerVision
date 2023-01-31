import numpy as np
import cv2

"""
- Conectar funções com callback
- Adicionando funcionalidades com eventos
- Usar o mouse
"""

print("\n--------- Desenhando com o mouse ---------\n")

blank_img = np.zeros(shape=(512,512,3), dtype=np.int8)

def draw_cicle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: #botão esquerdo apertado
        cv2.circle(blank_img, (x,y), 10, (0,255,0), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(blank_img, (x,y), 10, (255,0,0), -1)

cv2.namedWindow(winname="DESENHAR")
cv2.setMouseCallback("DESENHAR", draw_cicle)

while True:
    cv2.imshow("DESENHAR", blank_img)
    
    key = cv2.waitKey(10)
    if key != -1: print(key)
    if cv2.getWindowProperty("DESENHAR", cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()

print("\n--------- Desenhando com o mouse 2 ---------\n")

blank_img = np.zeros(shape=(512,512,3), dtype=np.int8)
drawing = False
ix, iy = -1, -1

def draw_rect(event, x, y, flags, param):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(blank_img, (ix,iy), (x,y), (255,0,0), 1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(blank_img, (ix,iy), (x,y), (255,0,0), -1)


cv2.namedWindow(winname="DESENHAR")
cv2.setMouseCallback("DESENHAR", draw_rect)

while True:
    cv2.imshow("DESENHAR", blank_img)
    
    key = cv2.waitKey(10)
    if key != -1: print(key)
    if cv2.getWindowProperty("DESENHAR", cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()