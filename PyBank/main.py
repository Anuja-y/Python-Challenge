#import modules
import os
import csv

# Create and initialize variables
totalbudget = 0
netchangelist = []
averagechange = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
Results = []

# Import and Read budget_data.csv
csvpath = os.path.join('PyBank\Resources','budget_data.csv')
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) #skip header
    
    firstrow = next(csvreader)
    previousnet = int(firstrow[1]) 
    totalbudget = int(firstrow[1]) 

    # Loop through csv file
    for row in csvreader:
        
        #Capture data      
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
    
    # Calculate Average Change
    averagechange = sum(netchangelist)/len(netchangelist)

# Print results to terminal
print("Financial Analysis")
print("--------------------------------------------------------------")
print("Total Months:", (csvreader.line_num - 1))
print("Total: $",totalbudget)
print("Average Change: $",round((averagechange),2))
print("Greatest Increase in Profits:", greatest_increase[0],"($",greatest_increase[1],")")
print("Greatest Decrease in Profits:", greatest_decrease[0],"($",greatest_decrease[1],")")


# Write results to a text file
file = open("PyBank\Analysis\Results.txt","w")
file.writelines(f'\n Financial Analysis')
file.writelines(f"\n\n --------------------------------------------------------------")
file.writelines(f"\n\n Total Months: {csvreader.line_num - 1}")
file.writelines(f"\n\n Total: $ {totalbudget}")
file.writelines(f"\n\n Average Change: ${round((averagechange),2)}")
file.writelines(f"\n\n Greatest Increase in Profits: {greatest_increase[0]} ${greatest_increase[1]}")
file.writelines(f"\n\n Greatest Decrease in Profits: {greatest_decrease[0]} ${greatest_decrease[1]}")
file.close()