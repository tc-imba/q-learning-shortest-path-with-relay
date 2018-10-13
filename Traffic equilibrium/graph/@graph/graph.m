function g = graph(a,b)
%GRAPH graph class constructor
% g = graph: consturct an empty (directed) graph
% g = graph(g0): construct a copy of graph g0
% g = graph(v,e): construct a graph 
% where
%   v:  a row vector of nodes; eg., [0,1,...,n]
%       note that node names start with 0; i.e., v(1) = 0!
%   e:  a column vector of edges; eg., [[0,1];[0,2];[1,3];...]

% TO DO:
% - node id starting with 0 is good to reduce revisions of figures, but unnatural!!

if nargin > 3
    error('Error: Number of arguments > 2');
elseif nargin == 0  % enmpty graph
    g.v = [];
    g.e = [];
    g.adj_v = cell(0,0);
    g.adj_e = cell(0,0);
    g = class(g,'graph');
elseif nargin == 1 & isa(a,'graph') % copy of graph a
    g = a;
elseif nargin ==  2 
    if isnumeric(a) & size(a,1) == 1 
        if isnumeric(b) & size(b,2) == 2
            n = size(a,2); 
            m = size(b,1);  
            % if a == cumsum(ones(1,n))  % node set must be row vector [1,2,...,n]
            if a == [0,cumsum(ones(1,n-1))]  % node set must be row vector [0,1,...,n] for "C compatibility"..
                g.v = a;
                g.e = b;
                g.adj_v = cell(1,n);
                for i = 1:n
                    g.adj_v{i} = [];
                end
                g.adj_e = cell(1,n);
                for i = 1:m
                    g.adj_e{i} = [];
                end

                for j = 1:m
                    edge = g.e(j,:);
                    if ismember(edge(1),g.v) & ismember(edge(2),g.v)   % edge validity check
                        %if ~ismember(edge(2),g.adj_v{edge(1)}) % duplication check
                        %    g.adj_v{edge(1)} = [g.adj_v{edge(1)},edge(2)];
                        %    g.adj_e{edge(1)} = [g.adj_e{edge(1)},j];
                        if ~ismember(edge(2),g.adj_v{edge(1)+1}) % duplication check
                            g.adj_v{edge(1)+1} = [g.adj_v{edge(1)+1},edge(2)];
                            % g.adj_e{edge(1)+1} = [g.adj_e{edge(1)+1},j-1];
                            g.adj_e{edge(1)+1} = [g.adj_e{edge(1)+1},j];
                        else
                            error('Error: Edge set contains duplicated edges');
                        end
                    else
                        error('Error: Edges contain non-existing nodes.');
                    end
                end
                g = class(g,'graph');
            else
                % error('Error: Node set must be row vector [1,2,...,n]');
                error('Error: Node set must be row vector [0,1,...,n]');
            end
        else
            % error('Error: Edge set must be in the form [[1,2];[1,3];...]');
            error('Error: Edge set must be in the form [[0,1];[0,2];...]');
        end
    else
        % error('Error: Node set must be row vector [1,2,...,n]');
        error('Effor: Node set must be row vector [0,1,...,n]');
    end
end
