#modules
import os
import csv

# Set path for file
csvpath = os.path.join(".", "Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    
# create variables to store data
total_votes = 0
currentCandidate = "" # current candidates name
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
            # this is new candidate hence add them in the list of candidates
            candidates.append(currentCandidate)

            # also set the voting count to 1
            candidateVotes[currentCandidate] = 1
        else:
            # if they are already in the list just add the vote to the dictionary
            candidateVotes[currentCandidate] = candidateVotes[currentCandidate] + 1
   
      
                
print("Election Results")
print("----------------------")
print(f"Total Votes: {total_votes}")
print("----------------------")
for cv in candidateVotes:
    print(cv + ": " + str(round(((candidateVotes[cv]/total_votes)*100),3)) + "%" + " (" + str(candidateVotes[cv]) + ")")
print("----------------------")
# printing the winner 
# get values from dictionary & get max value of it
listVotes = list(candidateVotes.values())

# print based on dictionary value to pull the matching key
print("Winner: " + str(list(candidateVotes.keys())[list(candidateVotes.values()).index(max(listVotes))]))
print("\n")
print("----------------------")

# Specify the file to write to
output_path = os.path.join("..", "PyPoll", "Analysis", "file.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as file:
    file.write("Election results:")
    file.write("\n")
    file.write("-------------------------------------")
    file.write("\n")
    file.write("Total Votes: " + str(total_votes))
    file.write("\n")
    file.write("-------------------------------------")
    file.write("\n")
    for cv in candidateVotes:
        file.write(cv + ": " + str(round(((candidateVotes[cv]/total_votes)*100),6)) + "%" + " (" + str(candidateVotes[cv]) + ")") 
        file.write("\n")
    file.write("-------------------------------------")
    file.write("\n")
    file.write("Winner is " + str(list(candidateVotes.keys())[list(candidateVotes.values()).index(max(listVotes))]))
    file.write("\n")
    file.write("-------------------------------------")


