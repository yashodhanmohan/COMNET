from data_fetcher import *
from graph_tool.centrality import eigenvector
from graph_tool.draw import graph_draw, sfdp_layout
import matplotlib.pyplot as plt
from numpy import histogram

G = getContactNetwork(size=100, lib='graphtools')
# G = getCommonFriendsNetwork(size=100, lib='graphtools')
# G = getCommonSubscriptionsNetwork(size=100, lib='graphtools')
# G = getCommonSubscribersNetwork(size=100, lib='graphtools')
# G = getCommonFavoriteVideosNetwork(size=100, lib='graphtools')

largest_eigenvalue, eigenvector_centrality = eigenvector(G)
position = sfdp_layout(G, vweight=eigenvector_centrality, eweight=G.edge_properties["weight"])

graph_draw(G, pos=position, vertex_fill_color=eigenvector_centrality, output='EigenvectorGraph/contacts.png', fit_view=2)
# graph_draw(G, pos=position, vertex_fill_color=eigenvector_centrality, output='EigenvectorGraph/commonfriends.png', fit_view=3.8)
# graph_draw(G, pos=position, vertex_fill_color=eigenvector_centrality, output='EigenvectorGraph/commonsubscriptions.png', fit_view=3.8)
# graph_draw(G, pos=position, vertex_fill_color=eigenvector_centrality, output='EigenvectorGraph/commonsubscribers.png', fit_view=3.8)
# graph_draw(G, pos=position, vertex_fill_color=eigenvector_centrality, output='EigenvectorGraph/commonfavoritevideos.png', fit_view=3.8)