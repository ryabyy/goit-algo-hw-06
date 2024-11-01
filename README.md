**Goal:** Perform a graph analysis on a sample network structure using the three algorithms mentioned below.

**Algorithms used:**
- _DFS search_
- _BFS search_
- _Dijkstra shortest path_

**Network model:**
The model is a toy model for internet connection map, with users and a service. It consists of a number of elements, resembling the real concepts in the net. Below are the meanings behind each of the nodes used in the network graph:
U1 - User 1, as in the end-user at home or office
U2 - User 2, as in the end-user at home or office
U3 - User 3, as in the end-user at home or office
I - ISP (Internet Service Provider)
V - VPN (Virtual Private Network) provider
D - Domain address
S - Server or the host of a service
The weights used and depicted in the graph are approximations for difficulty/speed of the data transfer between the nodes. Here, all connections are used with a small weight of 1, while only the connection to the end-users is deemed slow at 5.

**Results:**
The analysis is performed, showing the amount of nodes, edges, and degree of the nodes, and whether the graph is connected. Also the DFS and BFS search algorithms are used for a walk over all graph nodes.
As expected, the DFS and BFS differ in that BFS would first cover all level-1 nodes connected to I, before going to visit the furthest node of S via D, while DFS would go deep in all connections of the nodes it meets.
Besides that, the Dijkstra algorithm of finding the shortest paths is used to find the shortest connections between each of the nodes present in the graph, reporting both the paths and the distances for each solution.
The results of the shortest paths finding process show that the slowest connections are between the end-users (U*), while to reach the S (server) node for any of the users it's faster/shorter to do that without visiting the V (VPN) node.
