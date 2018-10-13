function adj_e = get_adj_e(v,g)
%UGRAPH/GET_ADJ_E returns edge adjanceny list
% adj_e = get_adj_e(v,g)
% where
%   adj_e:  a row vector of indices of edges that are incident from v = 0,1,2...
%           Note that the index starts with 1!
%   v:      node in g
%   g:      ugraph object

if ismember(v,g.v)
    adj_e = g.adj_e{v+1}; % must be curly bracket {} as g.adj_e is cell array
else
    error('Error: node not found in graph');
end
