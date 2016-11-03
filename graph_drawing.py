from data_fetcher import *
from graph_tool.draw import graph_draw

# G = getContactNetwork(size=20, lib='networkx')
# G = getContactNetwork(size=20, lib='igraph')
G1 = getContactNetwork(size=100, lib='graphtools')
G2 = getCommonFriendsNetwork(size=100, lib='graphtools')
G3 = getCommonSubscriptionsNetwork(size=100, lib='graphtools')
G4 = getCommonSubscribersNetwork(size=100, lib='graphtools')
G5 = getCommonFavoriteVideosNetwork(size=100, lib='graphtools')

graph_draw(G1, output='Graph/contacts.png', fit_view=3)
graph_draw(G2, output='Graph/commonfriends.png', fit_view=3)
graph_draw(G3, output='Graph/commonsubscriptions.png', fit_view=3)
graph_draw(G4, output='Graph/commonsubscribers.png', fit_view=3)
graph_draw(G5, output='Graph/commonfavoritevideos.png', fit_view=3)