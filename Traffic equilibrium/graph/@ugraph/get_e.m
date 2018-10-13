function e = get_e(g)
%UGRAPH/GET_E accessor for edge set in graph object
% e = get_e(g)
% where
%   e:  column vector of edges, eg. [[0,1];[0,2];[1,3];...]
%       note that node names start with 0!
%   g:  ugraph object

e = g.e;