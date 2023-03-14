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

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    print(file_reader)