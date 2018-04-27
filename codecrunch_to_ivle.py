import csv
import math

dct = {}

'''
accepts csv files containing marks as input, combines and scales the marks,
stores in dct (above)
'''
def getMarks(*filenames):

    for i in filenames:
        with open(i) as csvfile:
            file_reader = csv.reader(csvfile)
            for row in file_reader:
                try:
                    if (row[1] not in dct):
                        dct[row[1]] = [float(row[-3])]
                    else:
                        dct[row[1]].append(float(row[-3]))
                #to handle the header
                except:
                    continue 
    
    for i in dct:
        if len(dct[i]) == 3:
            dct.sort() #sort in ascending order, select last 2 as the best 2 
            bestTwo = sum(dct[i][1:])
        elif len(dct[i]) in (1, 2): #if student submitted 1/2 entries, then just select them.
            bestTwo = sum(dct[i])
        else:
            bestTwo = 0
        dct[i] = math.ceil(bestTwo*100)/200 #round to 2 decimal places. 

'''
Uses data stored in dct to write to csv
'''
def write_to_file():

    with open("for_ivle_upload.csv", "w", newline='') as csvfile:

        filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', \
                                quoting=csv.QUOTE_MINIMAL)
        
        filewriter.writerow(["USER_ID","MARKS","REMARKS",\
                             "GRADES","MODERATIONS"])

        for student in dct:

            marks = dct[student]
            
            entry = [str(student), marks, "Please refer to Codecrunch. Average of best 2 scores taken. "]

            filewriter.writerow(entry)

