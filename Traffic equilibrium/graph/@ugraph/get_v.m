function v = get_v(g)
%GRAPH/GET_V accessor for node set in graph object
% v = get_v(g)
% where
%   v:  row vector of nodes, eg. [0,1,2,...].
%       note that node names start with 0; i.e., v(1) = 0!
%   g:  graph object

v = g.v;