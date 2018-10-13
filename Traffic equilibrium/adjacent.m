function [neighbors] = adjacent(node, edges)
%adjacent: return all the nodes that are adjacent to "node" 
%   node: the input node
%   edges: set of edges
neighbors = [];
for i = 1:size(edges, 1)
    if edges(i, 1) == node
        neighbors = [neighbors, edges(i, 2)];
    end
end
end

