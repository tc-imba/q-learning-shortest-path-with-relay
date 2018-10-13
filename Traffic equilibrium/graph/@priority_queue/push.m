function q = push(a,p,q)
%PRIORITY_QUEUE/PUSH add an element with a priority in q 
% q = push(a,p,q)
% where
%   a:       element to be added to q; must be a numeric scaler.
%            if a is already in q, a new copy of a is added with priority p.
%   p:       priority of element a
%   q (LHS): copy of q in RHS with a added 
%   q (RHS): priority queue object

if isnumeric(a) & size(a) == [1,1]
    if isnumeric(p) & size(p) == [1,1]
        ap = [a,p];
        q.list = [q.list;ap];
        q.list = sortrows(q.list,2); % sorted in ascending order of 2nd column (=priority)
    else
        error('Error: priority needs to be numeric scaler');
    end
else
    error('Error: only numeric scaler can be pushed');
end

