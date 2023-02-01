import matplotlib.pyplot as plt
import numpy as np
import cv2

print("""
--------- Gradiente de imagem ---------\n
- Mudança direcional na intensidade ou cor em uma imagem
- Usa 3x3 Kernels 
""")

sudoku = cv2.imread('./sudoku.jpg', 0)
plt.imshow(sudoku, cmap='gray')
plt.show()

sobel_x = cv2.Sobel(sudoku, cv2.CV_64F, 1, 0, ksize=5) #dx, ver vertical
sobel_y = cv2.Sobel(sudoku, cv2.CV_64F, 0, 1, ksize=5) #dy, ver horizontal
laplaciano = cv2.Laplacian(sudoku, cv2.CV_64F) #derivado em todas as dimenções

plt.imshow(sobel_x, cmap='gray')
plt.show()
plt.imshow(sobel_y, cmap='gray')
plt.show()
plt.imshow(laplaciano, cmap='gray')
plt.show()

blended = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
plt.imshow(blended, cmap='gray')
plt.show()

ret, threshold = cv2.threshold(blended, 100, 255, cv2.THRESH_BINARY)
plt.imshow(threshold, cmap='gray')
plt.show()

ret, threshold_inv = cv2.threshold(blended, 100, 255, cv2.THRESH_BINARY_INV)
plt.imshow(threshold_inv, cmap='gray')
plt.show()

kernel = np.ones((4,4), np.uint8)

gradient = cv2.morphologyEx(blended, cv2.MORPH_GRADIENT, kernel)
plt.imshow(gradient, cmap='gray')
plt.show()
