function display(q)
%STACK/DISPLAY Command window display of stack
% display(q)
% where
%   q:  stack object

max_chars = 50; % maximum number of characters displayed in one line

n = size(q.list,2);

fprintf(1,'\n');
fprintf(1,'%s =\n\n',inputname(1));
fprintf(1,'     ');
n_chars = 5;
if n == 0
    fprintf(1,'[]');
else
    fprintf(1,'[ ');
    n_chars = n_chars + 2;
    for i = 1:n
        if n_chars > max_chars
            fprintf(1,'\n');
            fprintf(1,'       ');
            n_chars = 7;
        end
        fprintf(1,'%g ',q.list(i));
        n_chars = n_chars + size(num2str(q.list(i)),2) + 1;
    end
    fprintf(1,'] ');
end
fprintf(1,'\n');


