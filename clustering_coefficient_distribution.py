from data_fetcher import *
from graph_tool.clustering import local_clustering
import matplotlib.pyplot as plt
from numpy import histogram

# G = getContactNetwork(size=100, lib='graphtools')
G = getCommonFriendsNetwork(size=100, lib='graphtools')
# G = getCommonSubscriptionsNetwork(size=100, lib='graphtools')
# G = getCommonSubscribersNetwork(size=100, lib='graphtools')
# G = getCommonFavoriteVideosNetwork(size=100, lib='graphtools')

clustering_coefficient = local_clustering(G)
count, bins = histogram(clustering_coefficient.get_array(), bins=100)
bins = 0.5*(bins[1:]+bins[:-1])

plt.plot(bins, count, '.', linewidth=2)
plt.yscale('log')
plt.grid(True)
plt.xlabel('Clustering coefficient, C')
plt.ylabel('Number of users')

# plt.savefig('Clustering coefficient distribution/contacts.png')
plt.savefig('Clustering coefficient distribution/commonfriends.png')
# plt.savefig('Clustering coefficient distribution/commonsubscriptions.png')
# plt.savefig('Clustering coefficient distribution/commonsubscribers.png')
# plt.savefig('Clustering coefficient distribution/commonfavoritevideos.png')
