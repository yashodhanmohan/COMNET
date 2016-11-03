from data_fetcher import *
from graph_tool.clustering import local_clustering
import matplotlib.pyplot as plt

# G = getContactNetwork(size=100, lib='graphtools')
# G = getCommonFriendsNetwork(size=100, lib='graphtools')
# G = getCommonSubscriptionsNetwork(size=100, lib='graphtools')
# G = getCommonSubscribersNetwork(size=100, lib='graphtools')
# G = getCommonFavoriteVideosNetwork(size=100, lib='graphtools')

degrees = G.degree_property_map(deg="total")
clustering_coefficient = local_clustering(G)

plt.plot(degrees.get_array(),clustering_coefficient.get_array(),'.', linewidth=2)
plt.xlabel('Degree, k')
plt.ylabel('Clustering coefficient, C(k)')

# plt.savefig('Clustering coefficient versus degree/contacts.png')
# plt.savefig('Clustering coefficient versus degree/commonfriends.png')
# plt.savefig('Clustering coefficient versus degree/commonsubscriptions.png')
# plt.savefig('Clustering coefficient versus degree/commonsubscribers.png')
# plt.savefig('Clustering coefficient versus degree/commonfavoritevideos.png')
