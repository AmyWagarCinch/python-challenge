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

# create variables to store data
total_votes = []
voter_id = []
candidate = []
candidate_names = []
percentage = []
vote_count = []
winner = 0
winner_candidate = ""

# Read the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        # Append the total votes and total ____ to their corresponding lists
        total_votes.append(row[0])
        candidate.append(row[2])
        
    # Create a list to keep candidate names
    for row in candidate: 
        if row not in candidate_names:
            candidate_names.append(row)
    # Count each candidate's votes and calculate percentage
    for name in candidate_names:
        count = 0
        for row in candidate:
            if name == row:
                count += 1
                percent = float(count) / float(total_votes) * 100
            if count > winner:
                winner = count
                winner_candidate = name
        # Insert data into the lists
        percentage.append(percent)
        vote_count.append(count)

        # Obtain the name's indexes for corresponding percentage and count variables
        x = candidate_names.index(name)
        
                
print("Election Results")
print("\n")
print("----------------------")
print("\n")
print(f"Total Votes: {len(total_votes)}")
print("\n")
print("----------------------")
print("\n")
print("f"{candidate_names[x]}: {percentage[x]:.3f}% ({vote_count[x]})\n"")
print("\n")
print("----------------------")
print(f"Winner: {winner_candidate}")
print("\n")
print("----------------------")
