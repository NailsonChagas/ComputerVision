import matplotlib.pyplot as plt
import numpy as np
import cv2

print("""
----------- Detecção de Objetos -----------\n
Objetivos da seção:
- Entender diversos modos de de detecção de objetos 

Tipos de de detecção de objetos:
1 - Template Matching: 
    * Procurar uma cópia exata de uma imagem em outra imagem
2 - Corner Detection:
    * Procurar por cantos na imagem
3 - Edge Detection:
    * Procurar contornos generalizados de objetos
4 - Grid Detection:
    * Combina os metodos 2 e 3 para encontrar grids na imagem   
    * Utilizado em varias aplicações
5 - Contour Detection:
    * Permite detectar o primeiro plano VS plano de fundo
    * Permite detectar contornos externos VS internos
6 - Feature matching:
    * Mais avançado meio de detectar objetos em imagens
    * Permite detectar um objeto, mesmo que na imagem não se possua
    uma cópia exata do objeto sendo procurado
7 - Watershed Algorithm:
    * Algoritmo avançado que permite segmentar uma imagem entre
    o primeiro plano e o segundo plano
8 - Facial and Eye Detection:
    * Utiliza Haar Cascades para detectar faces em imagens
    * Isso não é reconhecimento facial (para isso será utilizado Deep Learn)
""")
      
print("""
----------- Template Matching -----------\n
- Forma mais simples de detecção de objetos
- Não é generalizado
- Simplesmente percorre uma imagem maior procurando a existencia
de uma determinada imagem menor
- A principal opção que pode ser ajustada é o método de comparação
entre o objeto e a imagem
- Todos os métodos utilizam algum tipo de métrica de correção
""")

full_image = cv2.imread("./sammy.jpg")
full_image = cv2.cvtColor(full_image, cv2.COLOR_BGR2RGB)
plt.imshow(full_image)
plt.show() 

face = cv2.imread("./sammy_face.jpg")
face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
plt.imshow(face)
plt.show() 

biblioteca = "cv2"
metodos_de_comparacao = [
    "TM_CCOEFF",
    "TM_CCOEFF_NORMED",
    "TM_CCORR",
    "TM_CCORR_NORMED",
    "TM_SQDIFF",
    "TM_SQDIFF_NORMED",
]

for met in metodos_de_comparacao:
    full_img_copy = full_image.copy()
    met_aux = biblioteca + "." + met
    
    #eval verifica se string é alguma expreção em python -> no caso uma constante
    metodo = eval(met_aux) 

    res = cv2.matchTemplate(
        full_img_copy,
        face,
        metodo
    )

    min_value, max_value, min_loc, max_loc = cv2.minMaxLoc(res)

    if metodo in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    height, width, channels = face.shape

    bottom_right = (top_left[0] + width, top_left[1] + height)

    cv2.rectangle(full_img_copy, top_left, bottom_right, (255,0,0), thickness=3)
    
    plt.subplot(121)
    plt.imshow(res)
    plt.title("HEATMAP OF TEMPLATE MATCHING")
    
    plt.subplot(122)
    plt.imshow(full_img_copy)
    plt.title(f"Foto - {met}")
    
    plt.show() 