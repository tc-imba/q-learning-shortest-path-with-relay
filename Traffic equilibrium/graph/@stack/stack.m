function q = stack(a)
%STACK stack class constructor
% q = stack(): construc an empty stack
% q = stack(a): construc a copy of stack a
% where
%   a:  stack object

if nargin > 1
    error('Error: Number of arguments > 1');
elseif nargin == 0  % empty stack 
    q.list = [];
    q = class(q,'stack');
elseif nargin == 1 & isa(a,'stack') % copy of stack a
    q = a;
end