data = LOAD './reqddata.csv' USING PigStorage(',') AS (IndexNo:int, Name:chararray, Email:chararray, Created:chararray, Quantity:int, Itemname:chararray, Sku:chararray, Vendor:chararray);

reqddata = FOREACH data GENERATE Email, Created, Quantity, Itemname, Sku, Vendor;

sorted = ORDER reqddata BY Email, Created;

STORE sorted INTO './basketdata' USING PigStorage(',');



