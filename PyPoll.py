#How to retrieve data.
#Open the data file
#Wrtite down the names of all the candidate
#Get the total votes for each candidate
#Get the total votes cast for the election 

# Import dependencies
import csv
import os

# Open the elction results and read the file
file_to_load = os.path.join('Resources','election_results.csv')

# Create a file to write the analysis
file_to_save = os.path.join('Analysis', 'election_analysis.txt')

# Initiate variables
total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open file to start writing
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Get the headers
    headers = next(file_reader)
    
    #Count each row in the CSV file after skipping the header
    for row in file_reader:
        total_votes += 1

        # Get the candidate name for each row
        candidate_name = row[2]

        # Add the candidate name to the candidate list by reviewing if is already added or not
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            
            #Begin trackin candiadate's vote count
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

    with open(file_to_save, 'w') as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"--------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"--------------------------\n"
        )
        print(election_results, end="")
        txt_file.write(election_results)

        #Determine winning vote and candidate
        for candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes)/float(total_votes)*100

            #Print the total information
            candidate_results = (f'{candidate_name}: received {vote_percentage:.1f}% ({votes:,}) of total votes\n')
            print(candidate_results)
            txt_file.write(candidate_results)

            #Setting winning candidate and total winning vote count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name
            
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"---------------------------\n"
        )
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
    

