# -*- coding: UTF-8 -*-
"""PyPoll Homework Solution."""

#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

#Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------

# Incorporated the csv module

import os
import csv
# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("election_analysis.txt")

# Total Vote Counter
total_votes = 0

# Candidate Options and Vote Counters
candidate_options = []
candidate_votes = {}
results = []

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row...
    for row in reader:

        total_votes = total_votes + 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

outputhead = (       
f"-------------------------\n"
f"Election Results\n"
f"-------------------------\n"
f"Total votes: {total_votes}\n"
f"-------------------------")
print(f"{outputhead}")
for candidate in candidate_votes:
    votes = candidate_votes.get(candidate)
    vote_percentage = float(votes) / float(total_votes) * 100
    if (votes > winning_count):
        winning_count = votes
        winning_candidate = candidate
    voter_output = (f"{candidate}: {vote_percentage:.3f}% ({votes})")
    print(f"{voter_output}")
outputtail = (
f"-------------------------\n"
f"Winner: {winning_candidate}\n"
f"-------------------------")
print(f"{outputtail}")


with open(file_to_output, "w") as text_file:
    print(f"{outputhead}", file=text_file)
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        voter_output = (f"{candidate}: {vote_percentage:.3f}% ({votes})")
        print(f"{voter_output}", file=text_file)
    print(f"{outputtail}", file=text_file)
    