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
    #total_profit = 0
    #for row in csv.reader(csvfile):
        #total_profit += int(row[1])         
    #print(total_profit)
    
#count the number of months
#with open(csvpath) as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=",")
    #header = next(csvreader)
    
    #for row in csv.reader(csvfile):        
        #value = (len(list(csvfile))) + 1 
    #print(value)

# create empty lists for the following variables
total_months = []
total_profit = []
monthly_profit_change = []

# open csv file
with open(csvpath) as csvfile:
    # store the contents of the csv file in the variable csvreader
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip the header row
    header = next(csvreader)
    # loop through the rows stored in csvreader
    for row in csvreader:
        # Append the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        #Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
# Obtain the max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Correlate max and min to the correct month using month list and index from max and min
# Using the plus 1 at the end since month associated with change is the + 1 month or next month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1         
        
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
        
# Specify the file to write to
output_path = os.path.join("..", "PyBank", "Analysis", "file.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as file:
    
    file.write("```text")
    file.write("\n")
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
    file.write("\n")
    file.write("```")
