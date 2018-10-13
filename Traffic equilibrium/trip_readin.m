function [ flow_matric ] = trip_readin( trip_file, node_num )
%The function read in the trips file, and returns a matric shows the
%origin node and the destination node in the following format:
%   1   2   3   4
% 1 x11 x12 x13 x14
% 2 x21 x22 x23 z24
% 3 x31 x32 x33 x34
% 4 x41 x42 x43 x44
% xij means start from node i, and destination is node j
%   node_num: number of nodes in each block

%% clear the NANs, reshape the trips into one row
a = xlsread(trip_file);
a = a';
a = reshape(a,1,[]);
a(isnan(a)) = [];

%% reshape the row into target martrix
flow_matric = zeros(node_num);
origin_node = 0;
for i = 1:2:size(a,2)
    origin_node = ceil(i/(2*node_num)); % find origin node
    flow_matric(origin_node, a(i)) = a(i+1);
end
end

