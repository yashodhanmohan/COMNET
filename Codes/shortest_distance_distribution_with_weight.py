from data_fetcher import *
from graph_tool.stats import distance_histogram
from graph_tool import map_property_values
import matplotlib.pyplot as plt

# G = getContactNetwork(size=100, lib='graphtools')
# G = getCommonFriendsNetwork(size=100, lib='graphtools')
# G = getCommonSubscriptionsNetwork(size=100, lib='graphtools')
# G = getCommonSubscribersNetwork(size=100, lib='graphtools')
G = getCommonFavoriteVideosNetwork(size=100, lib='graphtools')

inverse_weight = G.new_edge_property('double')
G.edge_properties["inverse_weight"] = inverse_weight
map_property_values(G.edge_properties["weight"], G.edge_properties["inverse_weight"], lambda x: 1.0/x)

y, binEdges = distance_histogram(G, weight=G.edge_properties["inverse_weight"], bins=[0, 0.2])
bincenters = binEdges[:-1]
plt.plot(bincenters,y,'-', linewidth=2)
plt.yscale('log')
plt.xlabel('Shortest distance, k')
plt.ylabel('Number of paths')

# plt.savefig('Shortest distance distribution with weight/contacts.png')
# plt.savefig('Shortest distance distribution with weight/commonfriends.png')
# plt.savefig('Shortest distance distribution with weight/commonsubscriptions.png')
# plt.savefig('Shortest distance distribution with weight/commonsubscribers.png')
plt.savefig('Shortest distance distribution with weight/commonfavoritevideos.png')
