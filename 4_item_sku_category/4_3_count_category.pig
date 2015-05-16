data = LOAD './categories_emails.csv' USING PigStorage(',') AS (Email:chararray, Item:chararray, Category:chararray);

grouped = group data by (Email,Category);

grp_count = FOREACH grouped GENERATE group, COUNT(data) as cou;

final_data = FOREACH grp_count GENERATE FLATTEN(group), cou;

STORE final_data INTO './categorycount' USING PigStorage(',');




