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
- Simplesmente percorre uma imagem maior procurando a existencia
de uma determinada imagem menor
- A principal opção que pode ser ajustada é o método de comparação
entre o objeto e a imagem
- Todos os métodos utilizam algum tipo de métrica de correção
""")

