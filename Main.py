import math
import copy
from Grafo import Grafo


g = Grafo()
gInicial = Grafo()

g.agregar_vertices("50-11")
g.agregar_vertices("50-12")
g.agregar_vertices("50-13")
g.agregar_vertices("50-14")
g.agregar_vertices("50-15")

g.agregar_vertices("51-11")
g.agregar_vertices("51-12")
g.agregar_vertices("51-13")
g.agregar_vertices("51-14")
g.agregar_vertices("51-15")

g.agregar_vertices("52-11")
g.agregar_vertices("52-12")
g.agregar_vertices("52-13")
g.agregar_vertices("52-14")
g.agregar_vertices("52-15")

g.agregar_vertices("53-11")
g.agregar_vertices("53-12")
g.agregar_vertices("53-13")
g.agregar_vertices("53-14")
g.agregar_vertices("53-15")

g.agregar_vertices("54-11")
g.agregar_vertices("54-12")
g.agregar_vertices("54-13")
g.agregar_vertices("54-14")
g.agregar_vertices("54-15")

g.agregar_vertices("51-11")
g.agregar_vertices("51-12")
g.agregar_vertices("51-13")
g.agregar_vertices("51-14")
g.agregar_vertices("51-15")

g.agregar_vertices("52-11")
g.agregar_vertices("52-12")
g.agregar_vertices("52-13")
g.agregar_vertices("52-14")
g.agregar_vertices("52-15")

g.agregar_vertices("53-11")
g.agregar_vertices("53-12")
g.agregar_vertices("53-13")
g.agregar_vertices("53-14")
g.agregar_vertices("53-15")

g.agregar_vertices("54-11")
g.agregar_vertices("54-12")
g.agregar_vertices("54-13")
g.agregar_vertices("54-14")
g.agregar_vertices("54-15")

# m_floyd, m_warshall = g.floyd_warshall()

# No dirigido.
g.agregar_arista("50-11", "50-12", 5, False)
g.agregar_arista("50-12", "50-13", 5, False)
g.agregar_arista("50-13", "50-14", 5, False)
g.agregar_arista("50-14", "50-15", 5, False)

g.agregar_arista("51-11", "51-12", 10, False)
g.agregar_arista("51-12", "51-13", 10, False)
g.agregar_arista("51-13", "51-14", 10, False)
g.agregar_arista("51-14", "51-15", 10, False)

g.agregar_arista("52-11", "52-12", 5, False)
g.agregar_arista("52-12", "52-13", 5, False)
g.agregar_arista("52-13", "52-14", 5, False)
g.agregar_arista("52-14", "52-15", 5, False)

g.agregar_arista("53-11", "53-12", 5, False)
g.agregar_arista("53-12", "53-13", 5, False)
g.agregar_arista("53-13", "53-14", 5, False)
g.agregar_arista("53-14", "53-15", 5, False)

g.agregar_arista("54-11", "54-12", 5, False)
g.agregar_arista("54-12", "54-13", 5, False)
g.agregar_arista("54-13", "54-14", 5, False)
g.agregar_arista("54-14", "54-15", 5, False)

g.agregar_arista("50-11", "51-11", 5, False)
g.agregar_arista("51-11", "52-11", 5, False)
g.agregar_arista("52-11", "53-11", 5, False)
g.agregar_arista("53-11", "54-11", 5, False)

g.agregar_arista("50-12", "51-12", 7, False)
g.agregar_arista("51-12", "52-12", 7, False)
g.agregar_arista("52-12", "53-12", 7, False)
g.agregar_arista("53-12", "54-12", 7, False)

g.agregar_arista("50-13", "51-13", 7, False)
g.agregar_arista("51-13", "52-13", 7, False)
g.agregar_arista("52-13", "53-13", 7, False)
g.agregar_arista("53-13", "54-13", 7, False)

g.agregar_arista("50-14", "51-14", 7, False)
g.agregar_arista("51-14", "52-14", 7, False)
g.agregar_arista("52-14", "53-14", 7, False)
g.agregar_arista("53-14", "54-14", 7, False)

g.agregar_arista("50-15", "51-15", 5, False)
g.agregar_arista("51-15", "52-15", 5, False)
g.agregar_arista("52-15", "53-15", 5, False)
g.agregar_arista("53-15", "54-15", 5, False)

gInicial = copy.deepcopy(g)
# g.agregar_vertices("A")
# g.agregar_vertices("B")
# g.agregar_vertices("C")
# g.agregar_vertices("D")
# g.agregar_vertices("E")
# g.agregar_vertices("F")

# g.agregar_vertices("G")
# g.agregar_vertices("H")
# g.agregar_vertices("I")
# g.agregar_vertices("J")
# g.agregar_vertices("K")

# g.agregar_arista("A", "B", 5, False)
# g.agregar_arista("A", "D", 4, False)
# g.agregar_arista("A", "E", 2, False)
# g.agregar_arista("B", "C", 1, False)
# g.agregar_arista("B", "E", 1, False)
# g.agregar_arista("C", "F", 5, False)
# g.agregar_arista("D", "C", 3, False)
# g.agregar_arista("D", "E", 3, False)
# g.agregar_arista("D", "F", 4, False)
# g.agregar_arista("E", "F", 8, False)

# g.agregar_arista("F", "G", 3, False)
# g.agregar_arista("F", "H", 2, False)
# g.agregar_arista("G", "H", 5, False)
# g.agregar_arista("G", "I", 1, False)
# g.agregar_arista("G", "J", 4, False)
# g.agregar_arista("I", "J", 2, False)
# g.agregar_arista("J", "K", 5, False)
# g.agregar_arista("I", "K", 4, False)


g.CaminoCortoJavierAndreina("54-14", "52-13", "50-14")

# g.imprimir_matriz(g.matriz, False)
# Encontrar la matriz de Andreina
# for i in range(gInicial.matriz.__len__()):
#     for a in range(gInicial.matriz[i].__len__()):
#         if gInicial.matriz[i][a] != None:
#             gInicial.matriz[i][a] += 2


# gInicial.imprimir_matriz(gInicial.matriz, False)
