function tf = ismember(a,q)
%QUEUE/ISMEMBER returns 1 if q contains a, 0 otherwise
% tf = ismember(a,q)
% where
%   tf: 1 if q contains a, 0 otherwise
%   a:  a numerical scaler
%   q:  queue object

tf = ismember(a,q.list);