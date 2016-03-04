# bigd




Remember that transform scripts in hive should receive data from STDIN and return results to
STDOUT.  So, to properly test  your transform script try this:
* hive -e "select id from test limit 10" > testout.txt
* cat testout.txt | python transform_value.py


