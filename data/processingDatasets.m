function processingDatasets()


fid1 = fopen('input.csv','r'); %# open csv file for reading
no=0;
newline ='';
fileID = fopen('output.csv','w');
ii = 0;
while ~feof(fid1)
    ii = ii+1;
    line = fgets(fid1); %# read line by line
    if not (isequal(strtrim(newline) , strtrim(line))) 
        if no > 0
        fprintf(fileID,'%s\n', strcat(newline,',',num2str(no)));
        end
        newline = line;       
        no = 1;
        
    else
        no = no + 1;
    end
    if rem(ii,100000) == 0
       disp(ii); 
    end
end
fprintf(fileID,'%s\n', strcat(newline,',',num2str(no)));
fclose(fid1);
fclose(fileID);


end