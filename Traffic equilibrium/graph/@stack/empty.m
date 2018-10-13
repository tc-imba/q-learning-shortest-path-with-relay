function tf = empty(q)
%STACK/EMPTY returns 1 if q is empty, 0 otherwise
% tf = empty(q)
% where
%   tf: 1 if q is empty, 0 otherwise
%   q:  stack object

tf = (size(q.list,2) == 0);
