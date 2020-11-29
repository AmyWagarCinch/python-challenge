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
candidates = []
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
            

print(f"Total Votes Cast: {len(total_votes)}")