function q = set_priority(a,p,q)
%SET_PRIORITY set the priority of element a in q
% q = set_priority(a,p,q)
% where
%   a:       element whose priority value is updated; 
%            must be a numeric scaler already in q
%   p:       new priority of element a
%   q (LHS): copy of q in RHS with priority of a set to p
%   q (RHS): priority queue object

if isnumeric(a) & size(a) == [1,1]
    if isnumeric(p) & size(p) == [1,1]
        [tf,i] = ismember(a,q.list(:,1));
        if tf == 1
            q.list(i,2) = p;
            q.list = sortrows(q.list,2); % sorted in ascending order of 2nd column (=priority)
        else
           error('Error: element not found in q'); 
        end
    else
        error('Error: priority needs to be numeric scaler')
    end
else
    error('Error: element must be numeric scaler');
end
