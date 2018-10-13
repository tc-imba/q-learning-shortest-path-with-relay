function tf = empty(q)
%QUEUE/EMPTY returns 1 if q is empty, 0 otherwise
% tf = empty(q)
% where
%   tf: 1 if q is empty, 0 otherwise
%   q:  queue object

tf = (size(q.list,2) == 0);
