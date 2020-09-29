# The data we need to retrieve.
import os
import csv

file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter
total_votes = 0

# Declare an empty list
candidate_options = []

# Declare an empty dictionary
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    for row in file_reader:
        total_votes += 1
# A complete list of candidates who received votes
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

# The total number of votes each candidate won
        candidate_votes[candidate_name] += 1

# Iterate through candidate list
for candidate_name in candidate_votes:

# retrieve vote count of candidate
    votes = candidate_votes[candidate_name]

# The percentage of votes each candidate won
    vote_percentage = float(votes) / float(total_votes) * 100

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    if (votes > winning_count) and (vote_percentage > winning_percentage):

        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n"
)

print(winning_candidate_summary)





# 5. The winner of the election based on popular vote


with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")





