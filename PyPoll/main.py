# Import modules
import os
import csv
import operator as op

# Create and initialise variables
listofcandidates=[]
listofvotes = []
results = {}
previousvotes = 0

# Import and Read election_data.csv
csvpath = os.path.join('PyPoll\Resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
   
    firstrow = csv_header
    previouscandidate = firstrow[2]
    count = 0
    candidates = []

    # Loop through csv file
    for row in csvreader:
        
        # Create a list of all candidates
        candidates += [row[2]]

        # Create a list of actual candidates
        if row[2] != previouscandidate:
            candidate = row[2]
            listofvotes = [previousvotes]
            result = listofcandidates.count(candidate)
            if result == 0:
                listofcandidates += [candidate]
         
        previouscandidate = row[2]
    
    # Loop through the list of actual candidates and count votes for each candidate and find a Winner
    for candidate in listofcandidates:
        listofvotes += [candidates.count(candidate)]
        if candidates.count(candidate) == max(listofvotes):
            winner = candidate   
    listofvotes.pop(0)
    
    
# Print results to terminal    
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

#Write results to text file
file = open("PyPoll\Analysis\Results.txt","w")
file.writelines(f"\n Election Results")
file.writelines(f"\n\n ----------------------------------------------------------")
file.writelines(f"\n\n Total Votes: {csvreader.line_num - 1}")
file.writelines(f"\n\n ----------------------------------------------------------")
file.writelines(f'\n\n {listofcandidates[0]}: {round(((listofvotes[0]/(csvreader.line_num - 1))*100),3)}% ({listofvotes[0]})')
file.writelines(f'\n\n {listofcandidates[1]}: {round(((listofvotes[1]/(csvreader.line_num - 1))*100),3)}% ({listofvotes[1]})')
file.writelines(f'\n\n {listofcandidates[2]}: {round(((listofvotes[2]/(csvreader.line_num - 1))*100),3)}% ({listofvotes[2]})')
file.writelines(f"\n\n ----------------------------------------------------------")
file.writelines(f"\n\n Winner: {winner}")
file.writelines(f"\n\n ----------------------------------------------------------")
file.close()