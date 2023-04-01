# Import modules
import os
import csv
votes = 0
listofcandidates=[""]
# Import and Read election_data.csv
csvpath = os.path.join('PyPoll\Resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f'CSV Header:{csv_header}')

    firstrow = next(csvreader)
    previouscandidate = firstrow[2]

    for row in csvreader:
        #print(row)

        if row[2] != previouscandidate:
            candidate = row[2]
            listofcandidates += candidate
            votes += 1
            
        else: 
            votes += 1
    print(listofcandidates)
    print(votes)

print("Total Votes:", (csvreader.line_num - 1))