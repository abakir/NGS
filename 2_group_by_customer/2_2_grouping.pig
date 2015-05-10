data = LOAD './dayhoursdata.csv' USING PigStorage(',') AS (IndexNo:int, Email:chararray, Quantity:int, Itemname:chararray, Sku:chararray, Vendor:chararray, Date:chararray, Time:chararray, Hours:int, Day:chararray);

reqddata = FOREACH data GENERATE Email, Quantity, Itemname, Sku, Vendor, Date, Time, Hours, Day;

sorted = ORDER reqddata BY Email;

STORE sorted INTO './groupdata' USING PigStorage(',');


