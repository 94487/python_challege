import csv
import os
# Read the election data from the CSV file
csvpath = os.path.join("C:\\Users\\gbegn\\python_challege\\Pypoll\\election_data.csv")
output_file = os.path.join("C:\\Users\\gbegn\\python_challege\\financial_analysis")

total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        # Count votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

        # Check for the winner
        if candidates[candidate] > winner_votes:
            winner = candidate
            winner_votes = candidates[candidate]

# Calculate the percentage of votes for each candidate
percentage_format = "{:.3%}"
candidate_results = []
for candidate, votes in candidates.items():
    percentage = votes / total_votes
    formatted_percentage = percentage_format.format(percentage)
    candidate_results.append(f"{candidate}: {formatted_percentage} ({votes})")

# Print and export results
output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{chr(10).join(candidate_results)}
-------------------------
Winner: {winner}
-------------------------
"""

print(output)

with open("financial_analysis", "w") as output_file:
    output_file.write(output)