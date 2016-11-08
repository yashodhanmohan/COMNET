from data_fetcher import *
from graph_tool.stats import distance_histogram
import matplotlib.pyplot as plt

# G = getContactNetwork(size=20, lib='networkx')
# G = getContactNetwork(size=20, lib='igraph')
# G = getContactNetwork(size=100, lib='graphtools')
# G = getCommonFriendsNetwork(size=100, lib='graphtools')
# G = getCommonSubscriptionsNetwork(size=100, lib='graphtools')
# G = getCommonSubscribersNetwork(size=100, lib='graphtools')
G = getCommonFavoriteVideosNetwork(size=100, lib='graphtools')

y, binEdges = distance_histogram(G)
bincenters = binEdges[:-1]
plt.plot(bincenters,y,'-', linewidth=2)
plt.yscale('log')
plt.xlabel('Shortest distance, k')
plt.ylabel('Number of paths')

# plt.savefig('Shortest distance distribution/contacts.png')
# plt.savefig('Shortest distance distribution/commonfriends.png')
# plt.savefig('Shortest distance distribution/commonsubscriptions.png')
# plt.savefig('Shortest distance distribution/commonsubscribers.png')
plt.savefig('Shortest distance distribution/commonfavoritevideos.png')
