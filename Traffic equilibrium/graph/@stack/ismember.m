function tf = ismember(a,q)
%STACK/ISMEMBER returns 1 if q contains a, 0 otherwise
% tf = ismember(a,q)
% where
%   tf: 1 if q contains a, 0 otherwise
%   a:  a numerical scaler
%   q:  stack object

tf = ismember(a,q.list);