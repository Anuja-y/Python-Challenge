#import modules
import os
import csv
totalbudget = 0
netchangelist = []
averagechange = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

# Import and Read budget_data.csv
csvpath = os.path.join('PyBank\Resources','budget_data.csv')
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f'CSV Header:{csv_header}')
    
    firstrow = next(csvreader)
    previousnet = int(firstrow[1]) 
    totalbudget = int(firstrow[1]) 
    for row in csvreader:
        print(row)
        #Capture data to calculate average change       
        totalbudget += int(row[1])
        netchange = int(row[1]) - previousnet
        netchangelist += [netchange]
        previousnet = int(row[1])

        # Calculate the greatest increase
        if netchange > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = netchange

        # Calculate the greatest decrease
        if netchange < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = netchange
    averagechange = sum(netchangelist)/len(netchangelist)

print("Financial Analysis")
print("----------------------------------------------")
print("Total Months:", (csvreader.line_num - 1))
print("Total:",totalbudget)
print("Average Change:",averagechange)
print("Greatest Increase in Profits:", greatest_increase)
print("Greatest Decrease in Profits:",greatest_decrease)
