
import os   # Importing the os module to create file paths across operating systems
import csv  # Module for reading CSV files

# Read the CSV file
election_data_csv = r"C:\Users\drabi\Assignments\Week3Challenge\PyPoll\Resources\election_data.csv"
election_results_text_file_path = r"C:\Users\drabi\Assignments\Week3Challenge\PyPoll\analysis\election_results.txt"

with open(election_data_csv, 'r') as file:  # Open the CSV file for reading
    csv_reader = csv.reader(file)   # Create a CSV reader object for the opened file
    next(csv_reader)  # Skip the header row
    csv_rows = list(csv_reader) # Convert the csv_reader iterator to a list and store it in the 'rows' variable

# Calculate the total number of votes cast in the election
total_votes = len(csv_rows)

# Create a set to store unique candidates
candidates = set()

# Create an empty dictionary
votes_candidate_dict = {} # Count the number of votes for each candidate

# Iterate through each row in csv_rows
for row in csv_rows:
    candidate = row[2]  # Get the candidate name from the third column of the current row
    candidates.add(candidate)   # Add the candidate to the set of unique candidates
    if candidate in votes_candidate_dict:
        votes_candidate_dict[candidate] += 1 # Increment the vote count for the candidate if the candidate already exists in the vote_candidate dictionary 
    else:
        votes_candidate_dict[candidate] = 1  #Initialize the vote count for the candidate as 1 if the candidate does not exist in the dict

# Calculate the percentage of votes for each candidate
percentage_per_candidate = {}

"Iterate through each candidate and their vote count in the votes_candidate_dict dictionary"
for candidate, votes in votes_candidate_dict.items():
    percentage = (votes / total_votes) * 100    # Calculate the percentage of votes for the current candidate
    percentage_per_candidate[candidate] = round(percentage, 3)  # Round the percentage to 3 decimal places

# Find the winner
winner = max(votes_candidate_dict, key=votes_candidate_dict.get)    # Get the candidate with the highest vote count

# Print the election results
print("\nElection Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Print the results for each candidate
for candidate in candidates:
    percentage = percentage_per_candidate[candidate]
    votes = votes_candidate_dict[candidate]
    print(f"{candidate}: {percentage}% ({votes})")

# Print the election results in console
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------\n")

# Write the election results to a text file
#election_results_file = "election_results.txt"

# Open the file in write mode, creating it if it doesn't exist, and assign it to the 'file' variable
with open(election_results_text_file_path, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")

    # Write the results for each candidate
    for candidate in candidates:
        percentage = percentage_per_candidate[candidate]
        votes = votes_candidate_dict[candidate]
        file.write(f"{candidate}: {percentage}% ({votes})\n")

    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

print("Please see election_results.txt for the election results.\n")


