from paa191t1.dijkstra import datastructs
import math
import heapq

class Heap(datastructs.DijkstraDistance):

    def __call__(self, nodes):

        self.__nodes = []

        self.__distances = [None] * len(nodes)

        self.__heap = []

        for node in nodes:
            self.__nodes.append(node)

            self.__distances[node] = math.inf

        return self


    def pop(self):
        node_pair = heapq.heappop(self.__heap)        

        return node_pair[1], node_pair[0]


    def update(self, node, distance):
        if distance == 0:
            self.__distances[node] = 0

            heapq.heappush(self.__heap, [self.__distances[node], node])

        else:
            self.__distances[node] = distance
            
            heapq.heappush(self.__heap, [self.__distances[node], node])


    def has_nodes_to_visit(self):
        """bool: Retorna verdadeiro se existe algum nó que ainda não foi visitado. Do contrário, falso."""
        return len(self.__heap) > 0

    def value(self, node):
        """Retorna a distância de um dado nó.
        Args:
            node (int): O nó
        """
        return self.__distances[node]

    @property
    def values(self):
        return dict([(k, v) for k, v in enumerate(self.__distances) if v is not None])