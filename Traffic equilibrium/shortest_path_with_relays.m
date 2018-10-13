%%
nodes = node + 1;
edges = edge + 1;
%% Define upper bound of weight
W = 20;
% Number of nodes in the graph
n = size(nodes, 2);
% Matrix with id of dominated path
L = zeros((W + 1), n);
% Define start node
s = 1;
% Define end node
t = 4;
% Define relay stations
relay = [];
% Define charging costs
rcost = zeros(1,size(nodes, 2));
% Define oil cost
ocost = fftime;
%% Start interation
nX = 1;
list = {};
% Initialize path, path cost = 0, cost spent on relay = 0, cummulative
% weight = 0, preceding path index = -1, last node = s.
list{nX, 1} = [0, 0, 0,-1, s];
X = [s];
while (~isempty(X))
    x = X(1);
    X = X(2:end);
    i = list{x, 1}(5);
    neighbors = adjacent(i, edges);
    for k= 1:size(neighbors, 2)
        j = neighbors(k);
        old_cost = list{x, 1}(1);
        relay_old_cost = list{x, 1}(2);
        oil_old_cost = list{x, 1}(3);
        cost = weight(i, j, edges, fftime);
        oil_cost = weight(i, j, edges, ocost);
        d = oil_old_cost + oil_cost;
        if d <= W
            if i ~= t
                new_cost = (old_cost + cost);
                if (L(1,j) == 0) || (L(1,j) ~= 0 && (new_cost < list{L(1,j),1}(1)))
                    relay_cost = relay_old_cost + rcost(j);
                    nX = nX + 1;
                    list{nX, 1} = [new_cost, relay_cost, 0, x, j];
                    L(1, j) = nX;
                    X = [X, nX];
                end
            end
            if (L(d+1,j) == 0 || (L(d+1,j) ~=0 && (list{x, 1}(1) + cost) < list{L(d+1,j),1}(1)))
                new_cost = (old_cost + cost);
                nX = nX + 1;
                list{nX, 1} = [new_cost, relay_old_cost, d, x, j];
                L(d+1,j) = nX;
                X = [X, nX];
            end
        end
    end
end