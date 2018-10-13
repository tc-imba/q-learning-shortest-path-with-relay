function [cost] = weight(node1, node2, edges, fftime)
%weight: return the weight between two nodes
%   node1: start node
%   node2: end node
%   fftime: can be modified to real cost in theis function
for i = 1:size(edges, 1)
    if node1 == edges(i,1) && node2 == edges(i,2)
        cost = fftime(i);
    end
end
end

