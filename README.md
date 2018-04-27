Simple python script which converts the codecrunch csv marks file to a format which is recognized by ivle gradebook. 

Chooses the best two out of three marks to average out and arrive at the final score. Tweak accordingly according to the grading needs. Should be quite trivial to you if you are reading this! :)  


`Remark.`

Output file will still be in csv format, but ivle requires xls/xlsx format. Use a spreadsheet editor (eg. excel, google sheet) to convert the csv file into xls or xlsx format.

`Remark. `

Can take in any number of files (using Python's * operator). But make sure no duplicate entries, or the calculation will likely go wrong. 

`Remark.` 

For Python 3, won't work on Python 2. 
