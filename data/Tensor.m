function tensor()
% load estimated subtensor by algorithms
data = readtable('output/xblock_3.tuples.csv','Delimiter', ','); 
data.Properties.VariableNames = {'protocol', 'service', 'flag', 'sbytes', 'dbytes', 'counts', 'srvcounts', 'connections'};
no_connection = size(data,1);
no=0;
disp(no_connection);
% load source find to get groundtruth
source = readtable('output/airforcel.csv','Delimiter', ','); 
source.Properties.VariableNames = {'protocol', 'service', 'flag', 'sbytes', 'dbytes', 'counts', 'srvcounts', 'connections','type'};
no_source = size(source,1);
disp(no_source);
% 'GroupCount' field
grp = grpstats (data, {'protocol', 'service', 'flag', 'sbytes', 'dbytes', 'counts', 'srvcounts', 'connections'});
[n,m]=size(grp);

attacksize = 0; 
for k=1:n % loop each row of each group
 r=grp(k,:);
 count = r{:,'GroupCount'}; 
 find = source(string(source.protocol)==r.protocol & string(source.service)==r.service & string(source.flag)==r.flag ...
     & source.sbytes==r.sbytes & source.dbytes==r.dbytes & source.counts ==r.counts & source.srvcounts ==r.srvcounts, :);
 find = find(1:count,:);
 attack = find(lower(string(find.type)) ~= 'normal.',:);
 attacksize = attacksize + size(attack,1);
 %
end


fprintf(' number of connections is %d, attack is %d, false positive is %d.',  no_connection, attacksize, no_connection-attacksize);

end