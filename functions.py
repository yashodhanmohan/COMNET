## g - Graph. can be created as -

import csv
import graph_tool.all as bakchodi

g = bakchodi.Graph()
e_weight = g.new_edge_property("float")
f_network = open('data/20_/1-edges', 'r')
reader_network = csv.reader(f_network, delimiter=delimiter)
for edge in reader_network:
     e = g.add_edge(int(edge[0]), int(edge[1]))
     e_weight[e] = float(edge[2])
f_network.close()


# Pagerank - Calculate the PageRank of each vertex.
graph_tool.centrality.pagerank(g, damping=0.85, pers=None, weight=None, prop=None, epsilon=1e-06, max_iter=None, ret_iter=False)

# Betweenness - Calculate the betweenness centrality for each vertex and edge.
graph_tool.centrality.betweenness(g, vprop=None, eprop=None, weight=None, norm=True)

# Central Point Dominance - Calculate the central point dominance of the graph, given the betweenness centrality of each vertex.
graph_tool.centrality.central_point_dominance(g, betweenness)

# Closeness - Calculate the closeness centrality for each vertex.
graph_tool.centrality.closeness(g, weight=None, source=None, vprop=None, norm=True, harmonic=False)

# Eigenvector - Calculate the eigenvector centrality of each vertex in the graph, as well as the largest eigenvalue.
graph_tool.centrality.eigenvector(g, weight=None, vprop=None, epsilon=1e-06, max_iter=None)

# Katz - Calculate the Katz centrality of each vertex in the graph.
graph_tool.centrality.katz(g, alpha=0.01, beta=None, weight=None, vprop=None, epsilon=1e-06, max_iter=None, norm=True)

# Hits - Calculate the authority and hub centralities of each vertex in the graph.
graph_tool.centrality.hits(g, weight=None, xprop=None, yprop=None, epsilon=1e-06, max_iter=None)

# Eigentrust - Calculate the eigentrust centrality of each vertex in the graph.
graph_tool.centrality.eigentrust(g, trust_map, vprop=None, norm=False, epsilon=1e-06, max_iter=0, ret_iter=False)

# Trust Transitivity - Calculate the pervasive trust transitivity between chosen (or all) vertices in the graph.
graph_tool.centrality.trust_transitivity(g, trust_map, source=None, target=None, vprop=None)