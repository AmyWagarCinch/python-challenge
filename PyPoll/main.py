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
total_votes = 0
#voter_id = []
#candidate = []
#candidate_names = []
#percentage = []
#vote_count = []
#winner = 0
#winner_candidate = ""
currentCandidate = "" # holds current candidates name
candidateVotes = {} # has key value pair of each candidate & their votes
candidates = [] # has list of all candidates names

# Read the csv file
with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        # Append the total votes and total numbers to their corresponding lists
        #total_votes.append(row[0])
        #candidate.append(row[2])
        total_votes = total_votes + 1
        currentCandidate = row["Candidate"]

        if currentCandidate not in candidates:
            # this is new candidate hence add him in the list of candidates
            candidates.append(currentCandidate)

            # also set his voting count to 1
            candidateVotes[currentCandidate] = 1
        else:
            # he is already in the list just add his vote to the dictionary
            candidateVotes[currentCandidate] = candidateVotes[currentCandidate] + 1
        
      
                
print("Election Results")
#print("\n")
print("----------------------")
#print("\n")
#print(f"Total Votes: {len(total_votes)}")
print(f"Total Votes: {total_votes}")
#print("\n")
print("----------------------")
#print("\n")
for cv in candidateVotes:
    print(cv + ": " + str(round(((candidateVotes[cv]/total_votes)*100),3)) + "%" + " (" + str(candidateVotes[cv]) + ")")
#print("f"{candidate_names[x]}: {percentage[x]:.3f}% ({vote_count[x]})\n"")
#print("\n")
print("----------------------")
#print(f"Winner: {winner_candidate}")
# printing the winner 
# get values from dictionary & get max value of it
listVotes = list(candidateVotes.values())

# print based on dictionary value to pull the matching key
print("Winner: " + str(list(candidateVotes.keys())[list(candidateVotes.values()).index(max(listVotes))]))
print("\n")
print("----------------------")

# Specify the file to write to
#output_path = os.path.join("..", "PyPoll", "Analysis", "file.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, 'w') as file:
