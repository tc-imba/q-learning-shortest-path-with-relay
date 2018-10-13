% change the following path, make sure the package "graph" is added
addpath('C:\Users\John_\Desktop\Traffic equilibrium\graph');
% nodes; must be [0,1,2,...]
% edges; must column vector
% capacity: capacity of each road (upper bound for free flow)
% fftime: free flow time, time need to pass the road when free flow
[node, edge, capacity, fftime] = net_readin('SiouxFalls_net');
[od_matric] = trip_readin('SiouxFalls_trips',24); %origin-destination matric