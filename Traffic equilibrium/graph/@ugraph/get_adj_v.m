function adj_v = get_adj_v(v,g)
%UGRAPH/GET_ADJ_V returns node adjanceny list
% adj_v = get_adj_v(v,g)
% where
%   adj_v:  a row vector of nodes in g that are adjacent to v = 0,1,2...
%           note that node names start with zero
%   v:      node in g
%   g:      ugraph object

if ismember(v,g.v)
    adj_v = g.adj_v{v+1}; % must be curly bracket {} as g.adj_v is cell array
else
    error('Error: node not found in graph');
end
