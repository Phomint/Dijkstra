import heapq
import sys

class Grafo:

    def __init__(self):
        self.vertices = {}

    def matrizAdjacente(self, local):

          arq = open(local, 'r')

          for linha in arq.readlines():
            posicao = linha.split()
            vertice1 = posicao[0]
            vertice2 = posicao[1]
            distancia = float(posicao[2])

            if vertice1 not in g.vertices:
                g.vertices.__setitem__(vertice1, {vertice2: distancia})

            if vertice2 not in g.vertices:
                g.vertices.__setitem__(vertice2, {vertice1: distancia})

            if vertice2 not in g.vertices.get(vertice1):
                g.vertices.get(vertice1).__setitem__(vertice2, distancia)

            if vertice1 not in g.vertices.get(vertice2):
                g.vertices.get(vertice2).__setitem__(vertice1, distancia)

          arq.close()

    def menorDistancia(self, origem, destino ):
        distancia = {}
        anterior = {}
        no = []

        for vertice in self.vertices:
            if vertice == origem:
                distancia[vertice] = 0
                heapq.heappush(no, [0, vertice])
            else:
                distancia[vertice] = sys.maxsize
                heapq.heappush(no, [sys.maxsize, vertice])
            anterior[vertice] = None

        while no:
            menor = heapq.heappop(no)[1]

            if menor == destino:
                caminho = []
                while anterior[menor]:
                    caminho.append(menor)
                    menor = anterior[menor]
                return caminho

            if distancia[menor] == sys.maxsize:
                break

            for vizinho in self.vertices[menor]:
                alt = distancia[menor] + self.vertices[menor][vizinho]

                if alt < distancia[vizinho]:
                    distancia[vizinho] = alt
                    anterior[vizinho] = menor
                    for n in no:
                        if n[1] == vizinho:
                            n[0] = alt
                            break
                    heapq.heapify(no)
        return distancia

if __name__ == '__main__':
    g = Grafo()

    local = str(input('Local do a# Se houver um novo caminho mais curto, atualize nossa fila de prioridades (relaxe)rquivo para análise dijkstra: '))
    origem = str(input('Origem do caminho: '))
    destino = str(input('Destino do caminho: '))

    g.matrizAdjacente(local)
    print(g.menorDistancia(origem, destino))


