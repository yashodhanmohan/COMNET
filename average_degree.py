from data_fetcher import *
from numpy import mean

# G = getContactNetwork(size=100, lib='graphtools')
# G = getCommonFriendsNetwork(size=100, lib='graphtools')
# G = getCommonSubscriptionsNetwork(size=100, lib='graphtools')
# G = getCommonSubscribersNetwork(size=100, lib='graphtools')
G = getCommonFavoriteVideosNetwork(size=100, lib='graphtools')

# print 'Mean of contact network degrees : ' + str(mean(G.degree_property_map(deg="total").get_array()))
# print 'Mean of common friends network degrees : ' + str(mean(G.degree_property_map(deg="total").get_array()))
# print 'Mean of common subscriptions network degrees : ' + str(mean(G.degree_property_map(deg="total").get_array()))
# print 'Mean of common subscribers network degrees : ' + str(mean(G.degree_property_map(deg="total").get_array()))
print 'Mean of common favorite videos network degrees : ' + str(mean(G.degree_property_map(deg="total").get_array()))

