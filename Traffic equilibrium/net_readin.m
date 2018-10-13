function [ nodes, edges, capacity, length ] = net_readin(net_file)
%The function read in the net file, and reshape the information into nodes,
%edges, and construc the graph (map)
%   nodes are in format: [0, 1, 2, 3, ..., 22, 23], start from 0
%   edges are in format: [[1,2];[1,3];[2,1],[2,3]...], column vector

a = xlsread(net_file, 'B:F');
%% get the nodes
nodes = unique(a(:,1));
nodes = (nodes - 1)';
%% get the edges
a(:,1) = a(:,1) - 1;
a(:,2) = a(:,2) - 1;
edges = a(:,1:2);
%% get capacities
capacity = a(:, 3);
%% get length
length = a(:,4);
end

