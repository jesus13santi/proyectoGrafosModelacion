import math
import copy


class Grafo:

    def __init__(self):
        self.vertices = []
        self.matriz = [[None]*0 for i in range(0)]

    def imprimir_matriz(self, m, texto):
        cadena = ""

        for c in range(len(m)):
            cadena += "|" + str(self.vertices[c])

        cadena += "\n " + (" -" * len(m))

        for f in range(len(m)):
            cadena += "\n" + str(self.vertices[f]) + " |"
            for c in range(len(m)):
                if texto:
                    cadena += "\t" + str(m[f][c])
                else:
                    if f == c and (m[f][c] is None or m[f][c] == 0):
                        cadena += " " + "\\"
                    else:
                        if m[f][c] is None or math.isinf(m[f][c]):
                            cadena += " " + "X"
                        else:
                            cadena += " " + str(m[f][c])

        cadena += "\n"
        print(cadena)

    @staticmethod
    def contenido_en(lista, k):
        if lista.count(k) == 0:
            return False
        return True

    def esta_en_vertices(self, v):
        if self.vertices.count(v) == 0:
            return False
        return True

    def agregar_vertices(self, v):
        if self.esta_en_vertices(v):
            return False
        # Si no esta contenido.
        self.vertices.append(v)

        # Se redimenciona la matriz de adyacencia.
        # Para preparalarla para agregar más Aristas.
        filas = columnas = len(self.matriz)
        matriz_aux = [[None] * (filas+1) for i in range(columnas+1)]

        # Se recorre la matriz y se copia su contenido dentro de la matriz más grande.
        for f in range(filas):
            for c in range(columnas):
                matriz_aux[f][c] = self.matriz[f][c]

        # Se iguala la matriz a la matriz más grande.
        self.matriz = matriz_aux
        return True

    def agregar_arista(self, inicio, fin, valor, dirijida):
        if not (self.esta_en_vertices(inicio)) or not (self.esta_en_vertices(fin)):
            return False
        # Si estan contenidos en la lista de vertices.
        self.matriz[self.vertices.index(
            inicio)][self.vertices.index(fin)] = valor

        # Si la arista entrante no es dirijida.
        # Instancio una Arista en sentido contrario de Fin a Inicio.
        if not dirijida:
            self.matriz[self.vertices.index(
                fin)][self.vertices.index(inicio)] = valor
        return True

    def recorrido_anchura(self, inicio):
        if not self.esta_en_vertices(inicio):
            return None

        recorrido = []
        cola = deque([inicio])

        while len(cola) > 0:
            v_aux = cola.popleft()
            recorrido.append(v_aux)

            for i in range(len(self.matriz)):
                if self.matriz[self.vertices.index(v_aux)][i] is not None:
                    v_candidato = self.vertices[i]
                    if not self.contenido_en(recorrido, v_candidato) and not self.contenido_en(cola, v_candidato):
                        cola.append(v_candidato)

        return recorrido

    def recorrido_profundidad(self, inicio):
        if not self.esta_en_vertices(inicio):
            return None

        recorrido = []
        pila = [inicio]

        while len(pila) > 0:
            v_aux = pila.pop()

            if not self.contenido_en(recorrido, v_aux):
                recorrido.append(v_aux)

            condicion = True

            for i in range(len(self.matriz)):
                if self.matriz[self.vertices.index(v_aux)][i] is not None:
                    v_candidato = self.vertices[i]

                    if not self.contenido_en(recorrido, v_candidato) and condicion:
                        # Es como un Break.
                        condicion = False

                        pila.append(v_aux)
                        pila.append(v_candidato)

        return recorrido

    def obtener_sucesores(self, v):
        pos_vertice = self.vertices.index(v)

        list_sucesores = []

        for i in range(len(self.matriz)):
            if self.matriz[pos_vertice][i] is not None:
                list_sucesores.append(self.vertices[i])

        return list_sucesores

    # Aciclico.
    def camino(self, k, v2):
        # Con ciclos.
        return self.__camino(k, v2, [])

    def __camino(self, k, v2, visitados):
        if k == v2:
            return True

        visitados.append(k)
        sucesores = self.obtener_sucesores(k)

        for vertice in sucesores:
            if not self.contenido_en(visitados, vertice):
                if self.__camino(vertice, v2, visitados):
                    return True

        return False

    # Es un booleano que verifica si todos los nodos estan marcados
    def allMarked(self, marcados):
        for i in range(marcados.__len__()):
            if not marcados[i]:
                return False
        return True

    # Se utiliza para verificar el menor de los no marcados en un vector
    def MinValueNotMarqued(self, pesos, marcados):
        # Inicializamos min en un numero infinito 999
        min = 999

        # Se inicializa pos en una posicion imposible para guardar el valor luego
        pos = -1

        # Se recorre el vector de pesos
        for i in range(pesos.__len__()):

            # Si se encuentra un vertice menor que la variable auxiliar y que no este
            # Ligado a un vertice marcado se remplaza la posicion y se guarda el valor
            if pesos[i] < min and not marcados[i]:
                min = pesos[i]
                pos = i
        return pos

    # Se hace lo mismo que para pesosDijikstra con la diferencia que se retorna
    # Un vector de recorridos
    def RecorridoDijikstra(self, inicio):
        pesos = []
        recorridos = []
        marcados = []

        pesos = [999 for i in range(self.matriz.__len__())]
        marcados = [False for i in range(self.matriz.__len__())]
        recorridos = [0 for i in range(self.matriz.__len__())]
        pesos[self.vertices.index(inicio)] = 0

        while (not self.allMarked(marcados)):
            aux = self.MinValueNotMarqued(pesos, marcados)
            if aux == -1:
                break
            marcados[aux] = True
            for i in range(self.matriz.__len__()):
                if self.matriz[aux][i] != None:
                    p = self.matriz[aux][i]
                    if p + pesos[aux] < pesos[i]:
                        pesos[i] = p + pesos[aux]
                        recorridos[i] = self.vertices[aux]
        # print(recorridos)
        return recorridos

    # Se utiliza para verificar todos los pesos de los nodos para llegar a inicio
    def PesosDijikstra(self, inicio):
        pesos = []
        recorridos = []
        marcados = []

        # Se inicializan todos los nodos con un valor infinito en este caso 999
        pesos = [999 for i in range(self.matriz.__len__())]
        # Se crea una lista que contieen los espacios del tamano de la matriz con False
        # Verfica que los nodos ya esten recorridos
        marcados = [False for i in range(self.matriz.__len__())]

        # Colocamos una lista con 0 del tamano de la matriz original
        recorridos = [0 for i in range(self.matriz.__len__())]

        # Inicializamos la posicion del vertice inicial denro del vector de pesos
        # Con un peso de 0
        pesos[self.vertices.index(inicio)] = 0

        # Mientras que se encuentren vertices sin marcar dentro del vector Marcados
        # Se ejecuta
        while (not self.allMarked(marcados)):
            # Se inicializa una variable auxiliar con el menor valor de los vertices
            # No marcados que se encuentren dentro del vector pesos
            aux = self.MinValueNotMarqued(pesos, marcados)

            # Si no exite el valor termina el proceso
            if aux == -1:
                break
            # Se marca el vertice auxiliar dentro del vector de vertices marcados
            marcados[aux] = True

            # Se recorre la matriz de adyacencia
            # Buscando los vertices adyacentes a la variable auxiliar
            for i in range(self.matriz.__len__()):
                # Si existe un vertice adyacente al nodo auxiliar
                if self.matriz[aux][i] != None:
                    # Se intancia una variable p para guardar el peso
                    p = self.matriz[aux][i]

                    # Si el peso del vertice adyacente mas el peso del recorrido realizado
                    # es menor al peso del recorrido anterior dentro del vecto de pesos
                    # Se reemplaza
                    if p + pesos[aux] < pesos[i]:
                        pesos[i] = p + pesos[aux]
                        recorridos[i] = self.vertices[aux]
        # print(pesos)
        return pesos

    # Se hace para tomar el camino mas corto (Retorna una lista)
    def DijikstraCamino(self, inicio, fin):
        # Se obtienen todos los caminos de Dijkstra desde el nodo inicio
        recorridos = self.RecorridoDijikstra(inicio)

        # Se inicializa la lista de salidas con el nodo final
        salida = [fin]

        # Verificamos que el nodo inicio sea diferentre que el ultimo elemento
        # De la lista de salida y agregamos a la lista de salida
        while inicio != salida[salida.__len__()-1]:
            salida.append(
                recorridos[self.vertices.index(salida[salida.__len__()-1])])

        # Revertimos la lista para que quede en su forma original
        recorridos = list(reversed(salida))

        # Se retorna una lista con los recorridos
        return recorridos
        # while inicio != list(salida)[salida.__len__()-1]:

        #     salida += recorridos[self.vertices.index(
        #         list(salida)[salida.__len__()-1])]
        # salida = ''.join(reversed(salida))
        # recorridos = list(salida)
        # return recorridos
        # print(recorridos)

    # SE UTILIZA PARA CREAR EL GRAFO
    def DijikstraGrafo(self, inicio, fin):
        # Si la lista de vertices no contiene el vertice inicio o el vertice final
        # No se puede recorrer
        if self.vertices.index(inicio) == -1 or self.vertices.index(fin) == -1:
            return None
        # Se instancia un grafo para guardar la informacion
        g = Grafo()

        # Se encuentra el camino (Retorna una lista)
        recorrido = self.DijikstraCamino(inicio, fin)
        # print(recorrido)

        # Retorna la lista de pesos de los grafos
        pesos = self.PesosDijikstra(inicio)

        # Retorna el peso del grafo total
        pesosCamino = pesos[self.vertices.index(fin)]

        # Se agregan los vertices al nuevo grafo
        for i in recorrido:

            g.agregar_vertices(i)

        # Se agregan las aristas de los vertices del nuevo grafo
        # Con el peso en cada vertice desde el inicio hasta ese vertice
        for i in range(recorrido.__len__()-1):
            pesosAux = self.PesosDijikstra(recorrido[i])
            pesosCaminoAux = pesosAux[self.vertices.index(recorrido[i+1])]
            g.agregar_arista(
                recorrido[i], recorrido[i+1], pesosCaminoAux, True)

        return g

    # Se hace doble Dijkstra y se modifican las matrices
    def CaminoCortoJavierAndreina(self, inicioJavier, inicioAndreina, fin):
        g = copy.deepcopy(self)
        grafoSegundaVuelta = copy.deepcopy(self)
        gd = g.DijikstraGrafo(inicioJavier, fin)
        gdPesos = gd.PesosDijikstra(inicioJavier)
        # print(gPesos)
        # print(gd.imprimir_matriz(gd.matriz, False))
        print("Camino mas corto Javier:")
        print(gd.vertices)
        print("El camino mas corto para Javier es de" +
              " " + str(gdPesos[gdPesos.__len__()-1]))

        # Guarda el peso de Javier recorrido 1
        gdPesos1 = gdPesos[gdPesos.__len__()-1]
        # Se hace para cololar los nodos ya visitados por Javier
        # Que no sean visitados por Andreina
        for i in gd.vertices:
            # print(self.matriz[self.vertices.index(i)])
            for a in range(g.matriz[g.vertices.index(i)].__len__()):
                if g.matriz[g.vertices.index(i)][a] != None:
                    g.matriz[g.vertices.index(i)][a] = 999

            for a in g.matriz:
                if (a[0] != None):
                    a[0] = 99
        print("-------------------------")

        # Matriz con los pesos de Andreina
        # for i in range(g.matriz.__len__()):
        #     for a in range(g.matriz[i].__len__()):
        #         if g.matriz[i][a] != None and g.matriz[i][a] != 999:
        #             g.matriz[i][a] += 2

        print("Camino mas corto Andreina: ")
        gd2 = g.DijikstraGrafo(inicioAndreina, fin)
        pesosg2 = gd2.PesosDijikstra(inicioAndreina)
        print(gd2.vertices)
        print("El camino mas corto para Andreina es de " +
              " "+str(pesosg2[pesosg2.__len__()-1]+(2*pesosg2.__len__()-2)))
        # Guarda el peso de Andreina Recorrido 1
        gdPesos2 = pesosg2[pesosg2.__len__()-1]+(2*pesosg2.__len__()-2)
        # print(gd2.PesosDijikstra(inicioAndreina))

        if gdPesos1 > gdPesos2:
            resta1 = gdPesos1 - gdPesos2
            resultado1 = "Para que puedan llegar iguales Andreina debe salir " + \
                str(resta1) + " minutos antes que Javier"
            print("Para que puedan llegar iguales Andreina debe salir " +
                  str(resta1) + " minutos antes que Javier")

        elif gdPesos1 < gdPesos2:
            resta1 = gdPesos2 - gdPesos1
            resultado1 = "Para que puedan llegar iguales, Javier debe salir " + \
                str(resta1) + " minutos antes que Andreina"
            print("Para que puedan llegar iguales, Javier debe salir " +
                  str(resta1) + " minutos antes que Andreina")
        else:
            resultado1 = "Para que puedan llegar iguales pueden salir al mismo tiempo"
            print("Para que puedan llegar iguales pueden salir al mismo tiempo")

        print("--------------------SEGUNDA VUELTA--------------------")
        # Comienza con Andreina
        gdSegundaVuelta = grafoSegundaVuelta.DijikstraGrafo(
            inicioAndreina, fin)
        pesosgdSegundaVuelta = gdSegundaVuelta.PesosDijikstra(inicioAndreina)
        print(gdSegundaVuelta.vertices)
        print("El camino mas corto para Andreina es de " +
              " "+str(pesosgdSegundaVuelta[pesosgdSegundaVuelta.__len__()-1]+(2*pesosgdSegundaVuelta.__len__()-2)))

        # Guarda el peso de Andreina recorrido 2
        gdPesos3 = pesosgdSegundaVuelta[pesosgdSegundaVuelta.__len__(
        )-1]+(2*pesosgdSegundaVuelta.__len__()-2)
        for i in gdSegundaVuelta.vertices:
            # print(self.matriz[self.vertices.index(i)])
            for a in range(grafoSegundaVuelta.matriz[grafoSegundaVuelta.vertices.index(i)].__len__()):
                if grafoSegundaVuelta.matriz[grafoSegundaVuelta.vertices.index(i)][a] != None:
                    grafoSegundaVuelta.matriz[grafoSegundaVuelta.vertices.index(
                        i)][a] = 999

            for a in grafoSegundaVuelta.matriz:
                if (a[0] != None):
                    a[0] = 99
        print("-------------------------")
        # JAVIER SEGUNDA VUELTA
        gd2SegundaVuelta = grafoSegundaVuelta.DijikstraGrafo(
            inicioJavier, fin)
        pesosgd2SegundaVuelta = gd2SegundaVuelta.PesosDijikstra(inicioJavier)
        print(gd2SegundaVuelta.vertices)
        print("El camino mas corto para Javier es de " +
              " "+str(pesosgd2SegundaVuelta[pesosgd2SegundaVuelta.__len__()-1]))

        # Guarda el peso de Javier recorrido 2
        gdPesos4 = pesosgd2SegundaVuelta[pesosgd2SegundaVuelta.__len__()-1]

        if gdPesos4 > gdPesos3:
            resta2 = gdPesos4 - gdPesos3
            resultado2 = "Para que puedan llegar iguales Andreina debe salir " + \
                str(resta2) + " minutos antes que Javier"
            print("Para que puedan llegar iguales Andreina debe salir " +
                  str(resta2) + " minutos antes que Javier")

        elif gdPesos4 < gdPesos3:
            resta2 = gdPesos3 - gdPesos4
            resultado2 = "Para que puedan llegar iguales, Javier debe salir " + \
                str(resta2) + " minutos antes que Andreina"
            print("Para que puedan llegar iguales, Javier debe salir " +
                  str(resta2) + " minutos antes que Andreina")
        else:
            resultado2 = "Para que puedan llegar iguales pueden salir al mismo tiempo"

        print("-------RECORRIDO DEFINITIVO---------")
        if resta2 > resta1:
            print("El camino mas corto para Javier es de " +
                  " "+str(gdPesos1))
            print("El camino mas corto para Andreina es de " +
                  " "+str(gdPesos2))
            print(resultado1)
        if resta2 < resta1:
            print("El camino mas corto para Andreina es de " +
                  " "+str(gdPesos3))
            print("El camino mas corto para Javier es de " +
                  " "+str(gdPesos4))
            print(resultado2)
