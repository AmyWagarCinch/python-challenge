#modules
import os
import csv

# Set path for file
csvpath = os.path.join(".", "Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    #Loop through looking for the ___
    for row in csvreader:
        print(row)
        break

total_votes = []
total_profit = []
monthly_profit_change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        # Append the total votes and total ____ to their corresponding lists
        total_votes.append(row[0])
        #total_profit.append(int(row[1]))
    # Iterate through the profits in order to get the monthly change in profits
    #for i in range(len(total_profit)-1):
        #Take the difference between two months and append to monthly profit change
        #monthly_profit_change.append(total_profit[i+1]-total_profit[i])
print(f"Total Votes Cast: {len(total_votes)}")
#print(f"Total: ${sum(total_profit)}")
#print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")