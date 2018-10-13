function [a,q] = pop(q)
%STACK/POP pop an element at the end of q (LIFO) 
% [a,q] = pop(q)
% where
%   a: element located at the end of q; NaN if q is empty
%   q (LHS): copy of q in RHS with a removed
%   q (RHS): stack object

n = size(q.list,2);
if n ~= 0
    a = q.list(1,n);
    q.list = q.list(1,1:n-1);   % remove the last column
else
    a = NaN;
end
    
    
