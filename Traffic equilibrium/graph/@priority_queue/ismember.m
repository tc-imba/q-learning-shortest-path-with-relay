function tf = ismember(a,q)
%PRIORITY_QUEUE/ISMEMBER returns 1 if q contains element a, 0 otherwise
% tf = ismember(a,q)
% where
%   tf: 1 if q contains a, 0 otherwise
%   a:  a numerical scaler
%   q:  priority queue object

tf = ismember(a,q.list(:,1));