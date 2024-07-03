import copy
from geopy.distance import distance

from database.DAO import DAO
import networkx as nx
class Model:
    def __init__(self):
        self._providers = DAO.getProvider()
        self._grafo = nx.Graph()
        self._location = []

        self._solBest = []
        self._lunBest = 0

    def buildGraph(self, provider, soglia):
        self._grafo.clear()
        self._location = DAO.getNodi1(provider)

        self._grafo.add_nodes_from(self._location)

        for u in self._location:
            for v in self._location:
                if u!=v:
                    distanza = distance((u.latitude, u.longitude), (v.latitude, v.longitude)).km

                    if distanza <= soglia:
                        if distanza < 0:
                            distanza = -distanza

                        self._grafo.add_edge(u, v, weight=distanza)




    def getNumNodes(self):
        return len(self._grafo.nodes)
    def getNumEdges(self):
        return len(self._grafo.edges)

    def trovaVicini(self):
        conPiuvicini = []
        lunMaggiore = 0

        for node in self._grafo.nodes:
            if len(list(self._grafo.neighbors(node))) > lunMaggiore:
                lunMaggiore = len(list(self._grafo.neighbors(node)))
                conPiuvicini = [node]
            elif len(list(self._grafo.neighbors(node))) == lunMaggiore:
                conPiuvicini.append(node)


        return conPiuvicini, lunMaggiore


    def getPercorso(self, target, stringa):
        self._solBest = []
        self._lunBest = 0

        for node in self._grafo.nodes:
            parziale = [node]
            self._ricorsione(parziale, stringa, target)

        return self._solBest

    def _ricorsione(self, parziale, stringa, target):

        if parziale[-1] == target:
            if len(parziale) > self._lunBest:
                self._lunBest = len(parziale)
                self._solBest = copy.deepcopy(parziale)
            return

        for node in self._grafo.neighbors(parziale[-1]):
            if stringa not in node.location and node not in parziale:
                parziale.append(node)
                self._ricorsione(parziale, stringa, target)
                parziale.pop()
