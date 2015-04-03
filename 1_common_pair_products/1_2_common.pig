data = LOAD './reqddata.csv' USING PigStorage(',') AS (IndexNo:int, Name:chararray, Email:chararray, Date:chararray, itemname:chararray, sku:chararray);

dump data;

grouped = group data by (sku);

dump grouped;

grp_count = FOREACH grouped GENERATE group, data, COUNT(data) AS kount;

dump grp_count;

mod_data = FILTER grp_count BY kount>1;

dump mod_data;

ord_data = ORDER mod_data BY kount DESC;

dump ord_data;

reqd_data = FOREACH ord_data GENERATE group, FLATTEN(BagToTuple(data.Name));

dump reqd_data;

STORE reqd_data INTO './modifydata' USING PigStorage(',');
