from data_fetcher import *
from graph_tool.clustering import local_clustering
import matplotlib.pyplot as plt

# G = getContactNetwork(size=100, lib='graphtools')
# G = getCommonFriendsNetwork(size=100, lib='graphtools')
# G = getCommonSubscriptionsNetwork(size=100, lib='graphtools')
# G = getCommonSubscribersNetwork(size=100, lib='graphtools')
# G = getCommonFavoriteVideosNetwork(size=100, lib='graphtools')

degrees = G.degree_property_map(deg="total").get_array()
clustering_coefficient = local_clustering(G).get_array()

# plt.plot(degrees,clustering_coefficient,'.', linewidth=2)
plt.plot(degrees,clustering_coefficient*degrees*(degrees-1),'.', linewidth=2)
plt.xlabel('Degree, k')
plt.ylabel('N(k)')

# plt.savefig('Clustering coefficient versus degree/contacts2.png')
# plt.savefig('Clustering coefficient versus degree/commonfriends2.png')
# plt.savefig('Clustering coefficient versus degree/commonsubscriptions2.png')
# plt.savefig('Clustering coefficient versus degree/commonsubscribers2.png')
# plt.savefig('Clustering coefficient versus degree/commonfavoritevideos2.png')
