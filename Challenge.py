import os
import csv

county_votes = {}

candidate_votes = {}

winning_county = ""

winning_candidate = ""

winning_count_county = 0

winning_count_candidate = 0

total_votes = 0

open_path = os.path.join("resources", "election_results.csv")

save_path = os.path.join("Analysis", "election_analysis_challenge.txt")

with open(open_path, "r") as open_data:
    read_data = csv.reader(open_data)
    headers = next(read_data)
    for row in read_data:
        county = row[1]
        candidate = row[2]
        if county not in county_votes:
            county_votes[county] = 0
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        county_votes[county] += 1
        candidate_votes[candidate] += 1
        total_votes += 1

with open(save_path, "w") as txt_file:

    statement_3 = (
        f"\nElection Results\n"
        f"--------------------------------\n"
        f"Total_Votes = {total_votes:,}\n"
        f"--------------------------------\n\n"
        f"County Votes:\n"
    )
    print(statement_3)
    txt_file.write(statement_3)

    for county in county_votes:
        votes_count = county_votes[county]
        votes_percentage = votes_count / total_votes * 100

        statement_1 = (
            f"{county}: {votes_percentage:.2f}% ({votes_count:,})\n"
        )
        print(statement_1)
        txt_file.write(statement_1)

        if votes_count > winning_count_county:
            winning_count_county = votes_count
            winning_county = county
            winning_percentage = winning_count_county/total_votes * 100

    statement_2 = (
        f"\n--------------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"--------------------------------\n"
    )
    print(statement_2)
    txt_file.write(statement_2)

    for candidate in candidate_votes:
        votes_count_candidate = candidate_votes[candidate]
        votes_percentage_candidate = votes_count_candidate / total_votes * 100

        statement_4 = (
            f"\n{candidate}: {votes_percentage_candidate:.2f}% ({votes_count_candidate:,})\n"
        )
        print(statement_4)
        txt_file.write(statement_4)

        if votes_count_candidate > winning_count_candidate:
            winning_count_candidate = votes_count_candidate
            winning_candidate = candidate
            winning_percentage_candidate = winning_count_candidate/total_votes * 100

    statement_5 = (
        f"\n--------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count_candidate:,}\n"
        f"Winning Percentage: {winning_percentage_candidate:.2f}%\n"
        f"--------------------------------\n"
    )
    print(statement_5)
    txt_file.write(statement_5)