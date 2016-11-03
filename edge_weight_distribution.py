from data_fetcher import *
from graph_tool.stats import edge_hist
import matplotlib.pyplot as plt

# G = getCommonFriendsNetwork(size=100, lib='graphtools')
# G = getCommonSubscriptionsNetwork(size=100, lib='graphtools')
# G = getCommonSubscribersNetwork(size=100, lib='graphtools')
G = getCommonFavoriteVideosNetwork(size=100, lib='graphtools')

y, binEdges = edge_hist(G, eprop=G.edge_properties["weight"])
bincenters = binEdges[:-1]
plt.plot(bincenters,y,'.-', linewidth=1)
plt.yscale('log')
plt.xlim(left=1)
# plt.xlabel('Number of common friends')
# plt.xlabel('Number of common subscriptions')
# plt.xlabel('Number of common subscribers')
plt.xlabel('Number of common favorite videos')
plt.ylabel('Number of Edges')

# plt.savefig('Edge weight distribution/commonfriends.png')
# plt.savefig('Edge weight distribution/commonsubscriptions.png')
# plt.savefig('Edge weight distribution/commonsubscribers.png')
plt.savefig('Edge weight distribution/commonfavoritevideos.png')
