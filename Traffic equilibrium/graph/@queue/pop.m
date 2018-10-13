function [a,q] = pop(q)
%QUEUE/POP pop an element at the beginning of q (FIFO) 
% [a,q] = pop(q)
% where
%   a: element located at the beginning of q; NaN if q is empty
%   q (LHS): copy of q in RHS with a removed
%   q (RHS): queue object

n = size(q.list,2);
if n ~= 0
    a = q.list(1,1);
    q.list = q.list(1,2:n); % remove the 1st colmun
else
    a = NaN;
end
    
    
