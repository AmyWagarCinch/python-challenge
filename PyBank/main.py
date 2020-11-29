#modules
import os
import csv

# Set path for file
csvpath = os.path.join(".", "Resources", "budget_data.csv")

#reading the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    #The net total amount of "Profit/Losses" over the entire period
    total_profit = 0
    for row in csv.reader(csvfile):
        total_profit += int(row[1])         
    print(total_profit)
    
#count the number of months
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    for row in csv.reader(csvfile):        
        value = (len(list(csvfile))) + 1 
    print(value)

total_months = []
total_profit = []
monthly_profit_change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        # Append the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        #Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
