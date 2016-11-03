from data_fetcher import *
from graph_tool.clustering import global_clustering
import matplotlib.pyplot as plt

# G1 = getContactNetwork(size=100, lib='graphtools')
# G2 = getCommonFriendsNetwork(size=100, lib='graphtools')
# G3 = getCommonSubscriptionsNetwork(size=100, lib='graphtools')
# G4 = getCommonSubscribersNetwork(size=100, lib='graphtools')
G5 = getCommonFavoriteVideosNetwork(size=100, lib='graphtools')

# clustering_coefficient1, std_dev1 = global_clustering(G1)
# clustering_coefficient2, std_dev2 = global_clustering(G2)
# clustering_coefficient3, std_dev3 = global_clustering(G3)
# clustering_coefficient4, std_dev4 = global_clustering(G4)
clustering_coefficient5, std_dev5 = global_clustering(G5)

# print 'Clustering coefficient for contacts network : ' + str(clustering_coefficient1)
# print 'Clustering coefficient for common friends network : ' + str(clustering_coefficient2)
# print 'Clustering coefficient for common subscriptions network : ' + str(clustering_coefficient3)
# print 'Clustering coefficient for common subscribers network : ' + str(clustering_coefficient4)
print 'Clustering coefficient for common favorite videos network : ' + str(clustering_coefficient5)