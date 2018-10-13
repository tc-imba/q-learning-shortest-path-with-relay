function display(q)
%PRIORITY_QUEUE/DISPLAY Command window display of priority queue
% display(q)
% where
%   q:  priority queue object

max_chars = 50; % maximum number of characters displayed in one line

n = size(q.list,1);

fprintf(1,'\n');
fprintf(1,'%s =\n\n',inputname(1));
fprintf(1,'     ');
n_chars = 5;
if n == 0
    fprintf(1,'[]');
else
    for i = 1:n
        if n_chars > max_chars
            fprintf(1,'\n');
            fprintf(1,'     ');
            n_chars = 5;
        end
        fprintf(1,'[ %g %g ] ',q.list(i,1),q.list(i,2));
        n_chars = n_chars + 2 + size(num2str(q.list(i,1)),2) ...
            + 1 + size(num2str(q.list(i,2)),2) + 3;
    end
end
fprintf(1,'\n\n');


