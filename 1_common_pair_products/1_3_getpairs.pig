register findpairs.py using jython as get;

data= LOAD './modifydata.csv' USING PigStorage(',') AS Sku:chararray;

final = FOREACH data GENERATE Sku, get.find($0, './modifydata.csv');

final1 = FOREACH final GENERATE Sku, FLATTEN(Name);

STORE final1 INTO './output' USING PigStorage(',');
