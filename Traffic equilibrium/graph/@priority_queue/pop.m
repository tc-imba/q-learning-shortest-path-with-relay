function [a,q] = pop(q)
%PRIORITY_QUEUE/POP pop an element with the minimum priority in q
% [a,q] = pop(q)
% where
%   a:       element (nmeric scaler) with the minimum priority in q; NaN if q is empty
%   q (LHS): copy of q in RHS with a removed
%   q (RHS): priority queue object

n = size(q.list,1);
if n ~= 0
    a = q.list(1,1);
    q.list = q.list(2:n,:); % remove the 1st row
else
    a = NaN;
end