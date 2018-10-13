function tf = empty(q)
%PRIORITY_QUEUE/EMPTY returns 1 if q is empty, 0 otherwise
% tf = empty(q)
% where
%   tf: 1 if q is empty, 0 otherwise
%   q:  priority queue object

tf = (size(q.list,1) == 0);
