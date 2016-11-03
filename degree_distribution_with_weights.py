from data_fetcher import *
from graph_tool.stats import vertex_hist
import matplotlib.pyplot as plt
from numpy import histogram

# G = getContactNetwork(size=20, lib='networkx')
# G = getContactNetwork(size=20, lib='igraph')
# G = getContactNetwork(size=100, lib='graphtools')
# G = getCommonFriendsNetwork(size=100, lib='graphtools')
# G = getCommonSubscriptionsNetwork(size=100, lib='graphtools')
# G = getCommonSubscribersNetwork(size=100, lib='graphtools')
# G = getCommonFavoriteVideosNetwork(size=100, lib='graphtools')

x = G.degree_property_map(deg="total", weight=G.edge_properties["weight"])
y = [i for i in x]

y, binEdges = histogram(y, bins=1000)
bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
plt.plot(bincenters,y,'.', linewidth=2)
plt.yscale('log')
plt.xlabel('Degree, k')
plt.ylabel('Number of users')

# plt.savefig('Degree distribution with weights/contacts.png')
# plt.savefig('Degree distribution with weights/commonfriends.png')
# plt.savefig('Degree distribution with weights/commonsubscriptions.png')
# plt.savefig('Degree distribution with weights/commonsubscribers.png')
# plt.savefig('Degree distribution with weights/commonfavoritevideos.png')
