from networkx import from_pandas_dataframe
from pandas import read_csv
from numpy import arange

nodes = [int(x) for x in open('data/nodes.csv').readlines()]

def getGraph(filepath):
    graph = from_pandas_dataframe(read_csv(filepath, header=None, names=['source', 'target', 'weight']), 'source', 'target', edge_attr='weight')
    graph.add_nodes_from(arange(1, len(nodes)+1))
    return graph

def getContactNetwork(size=100):
    return getGraph('data/'+str(size)+'%/1-edges.csv')

def getCommonFriendsNetwork(size=100):
    return getGraph('data/'+str(size)+'%/2-edges.csv')

def getCommonSubscriptionsNetwork(size=100):
    return getGraph('data/'+str(size)+'%/3-edges.csv')

def getCommonSubscribersNetwork(size=100):
    return getGraph('data/'+str(size)+'%/4-edges.csv')

def getCommonFavoriteVideosNetwork(size=100):
    return getGraph('data/'+str(size)+'%/5-edges.csv')
