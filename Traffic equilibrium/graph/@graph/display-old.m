function display(g)
%GRAPH/DISPLAY Command window display of graph
% display(g)
% where
%   g:  graph object

max_chars = 50; % maximum number of characters displayed in one line

n = size(g.v,2);
m = size(g.e,1);

% display g.v
fprintf(1,'\n');
fprintf(1,'%s.v =\n\n',inputname(1));
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
        fprintf(1,'%g ', g.v(i));
        n_chars = n_chars + size(num2str(g.v(i)),2) + 1;
    end
    fprintf(1,']');
end
fprintf(1,'\n');

% display g.e
fprintf(1,'\n');
fprintf(1,'%s.e =\n\n',inputname(1));
fprintf(1,'     ');
n_chars = 5;
if m == 0
    fprintf(1,'[]');
else
    for i = 1:m
        if n_chars > max_chars
            fprintf(1,'\n');
            fprintf(1,'     ');
            n_chars = 5;
        end
        edge = g.e(i,:);
        fprintf(1,'[ %g %g ] ',edge(1),edge(2));
        n_chars = n_chars + 2 + size(num2str(edge(1)),2) ...
            + 1 + size(num2str(edge(2)),2) + 3;
    end
end
fprintf(1,'\n');

% display g.adj_v
fprintf(1,'\n');
fprintf(1,'%s.adj_v =\n\n',inputname(1));
fprintf(1,'     ');
n_chars = 5;
if n == 0
    fprintf(1,'{}');
else
    for i = 1:n
        if n_chars > max_chars
            fprintf(1,'\n');
            fprintf(1,'     ');
            n_chars = 5;
        end
        adj_list = g.adj_v{i};
        k = size(adj_list,2);
        fprintf(1,'[ ');
        n_chars = n_chars + 2;
        for j = 1:k
            fprintf(1,'%g ',adj_list(j));
            n_chars = n_chars + size(num2str(adj_list(j)),2) + 1;
        end
        fprintf(1,'] ');
        n_chars = n_chars + 2;
    end
end
fprintf(1,'\n');

% display g.adj_e
fprintf(1,'\n');
fprintf(1,'%s.adj_e =\n\n',inputname(1));
fprintf(1,'     ');
n_chars = 5;
if n == 0
    fprintf(1,'{}');
else
    for i = 1:n
        if n_chars > max_chars
            fprintf(1,'\n');
            fprintf(1,'     ');
            n_chars = 5;
        end        
        adj_e_list = g.adj_e{i};
        k = size(adj_e_list,2);
        fprintf(1,'[ ');
        n_chars = n_chars + 2;
        for j = 1:k
            fprintf(1,'%g ', adj_e_list(j));
            n_chars = n_chars + size(num2str(adj_e_list(j)),2) + 1;
        end
        fprintf(1,'] ');
        n_chars = n_chars + 2;
    end
end
fprintf(1,'\n\n');
