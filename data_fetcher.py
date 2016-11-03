from pandas import read_csv
from numpy import arange
import networkx as nx
import igraph as ig
import graph_tool.all as gt
import csv

nodes = [int(x) for x in open('data/nodes.csv').readlines()]

def getGraph(filepath, lib):
    if lib=='networkx':
        graph = nx.from_pandas_dataframe(read_csv(filepath, header=None, names=['source', 'target', 'weight']), 'source', 'target', edge_attr='weight')
        graph.add_nodes_from(arange(1, len(nodes)+1))
        return graph
    elif lib=='graphtools':
        return gt.load_graph_from_csv(filepath, directed=False, eprop_types=['int'], eprop_names=['weight'])
    elif lib=='igraph':
        graph = ig.Graph()
        graph.add_vertices(len(nodes)+1)
        weights = []
        reader_network = csv.reader(open(filepath, 'r'))
        for edge in reader_network:
            graph.add_edge(int(edge[0]), int(edge[1]))
            weights.append(int(edge[2]))
        graph.es["weight"] = weights
        return graph

def getContactNetwork(size=100, lib='networkx'):
    return getGraph('data/'+str(size)+'_/1-edges.csv', lib)

def getCommonFriendsNetwork(size=100, lib='networkx'):
    return getGraph('data/'+str(size)+'_/2-edges.csv', lib)

def getCommonSubscriptionsNetwork(size=100, lib='networkx'):
    return getGraph('data/'+str(size)+'_/3-edges.csv', lib)

def getCommonSubscribersNetwork(size=100, lib='networkx'):
    return getGraph('data/'+str(size)+'_/4-edges.csv', lib)

def getCommonFavoriteVideosNetwork(size=100, lib='networkx'):
    return getGraph('data/'+str(size)+'_/5-edges.csv', lib)