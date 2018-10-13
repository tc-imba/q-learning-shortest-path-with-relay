function q = priority_queue(a)
%PRIORITY_QUEUE priority queue class constructor
% q = priority_queue(): construc an empty priority queue
% q = priority_queue(a): construc a copy of priority queue a
% where
%   a:  priority queue object

% members
%   q.list: colum vector of [a,p] where a = element and p = priority

if nargin > 1
    error('Error: Number of arguments > 1');
elseif nargin == 0  % empty priority queue
    q.list = [];
    q = class(q,'priority_queue');
elseif nargin == 1 & isa(a,'priority_queue') % copy of priority queue a
    q = a;
end