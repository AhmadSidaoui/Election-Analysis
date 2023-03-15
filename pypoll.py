# The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular votes

file_to_load = "Resources/election_results.csv"

election_data = open(file_to_load, 'r')

election_data.close()

# Opening and writing the election_results.csv file

import os
import csv

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

total_votes = 0

candidate_options = []

candidate_votes = {}

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    
    # Extracting the header row
    headers = next(file_reader)
    print(f"{headers}\n")

    # Counting and printing total_votes
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            
            # Initializing the candidate vote

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1 

    # Calculating the % of votes each candidate has

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes) * 100
        print(f"{candidate_name}: recieved {vote_percentage:.2f}% votes.\n")
    

    print(f"Total number of votes: {total_votes:,}\n")
    print(f"The candidates that are running are:\n{candidate_options}\n")
    print(f"The number of votes each candidate has:\n{candidate_votes}\n")
