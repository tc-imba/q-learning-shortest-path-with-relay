function q = queue(a)
%QUEUE queue class constructor
% q = queue(): construc an empty queue
% q = queue(a): construc a copy of queue a
% where
%   a:  queue object

if nargin > 1
    error('Error: Number of arguments > 1');
elseif nargin == 0  % empty queue
    q.list = [];
    q = class(q,'queue');
elseif nargin == 1 & isa(a,'queue') % copy of queue a
    q = a;
end