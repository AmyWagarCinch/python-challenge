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