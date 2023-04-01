# Import modules
import os
import csv
import operator as op

listofcandidates=[]
listofvotes = []
results = {}
previousvotes = 0
# Import and Read election_data.csv
csvpath = os.path.join('PyPoll\Resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f'CSV Header:{csv_header}')

    firstrow = csv_header
    previouscandidate = firstrow[2]
    count = 0
    candidates = []

    for row in csvreader:
        #print(row)
        candidates += [row[2]]
        if row[2] != previouscandidate:
            candidate = row[2]
            listofvotes = [previousvotes]
            result = listofcandidates.count(candidate)
            if result == 0:
                listofcandidates += [candidate]
         
        previouscandidate = row[2]
    
    for candidate in listofcandidates:
        listofvotes += [candidates.count(candidate)]
        if candidates.count(candidate) == max(listofvotes):
            winner = candidate   
    listofvotes.pop(0)
    #print(listofcandidates)
    #print(listofvotes)
    
    
print("Election Results")
print("----------------------------------------------------------")
print("Total Votes:", (csvreader.line_num - 1))
print("----------------------------------------------------------")
print(f'{listofcandidates[0]}: {round(((listofvotes[0]/(csvreader.line_num - 1))*100),3)}% ({listofvotes[0]})')
print(f'{listofcandidates[1]}: {round(((listofvotes[1]/(csvreader.line_num - 1))*100),3)}% ({listofvotes[1]})')
print(f'{listofcandidates[2]}: {round(((listofvotes[2]/(csvreader.line_num - 1))*100),3)}% ({listofvotes[2]})')
print("----------------------------------------------------------")
print("Winner:", winner)
print("----------------------------------------------------------")