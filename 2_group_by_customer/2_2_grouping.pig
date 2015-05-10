data = LOAD './dayhoursdata.csv' USING PigStorage(',') AS (IndexNo:int, Email:chararray, Quantity:int, Itemname:chararray, Sku:chararray, Vendor:chararray, Date:chararray, Time:chararray, Hours:int, Day:chararray);

reqddata = FOREACH data GENERATE Email, Quantity, Itemname, Sku, Vendor, Date, Time, Hours, Day;

grouped = group reqddata by (Email);

grp = FOREACH grouped GENERATE group, reqddata;

flat_data = FOREACH grp GENERATE FLATTEN(BagToTuple(reqddata));

dump flat_data;

STORE flat_data INTO './groupdata' USING PigStorage(',');


