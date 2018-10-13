function q = push(a,q)
%STACK/PUSH add an element at the end of q
% q = push(a,q)
% where
%   a:       element to be added at the end of q; must be numeric scaler
%            if a is already in q, a new copy of a is added.
%   q (LHS): copy of q in RHS with a added at the end
%   q (RHS): stack object

if isnumeric(a) & size(a) == [1,1]
    q.list = [q.list,a];
else
    error('Error: only numeric scaler can be pushed');
end

