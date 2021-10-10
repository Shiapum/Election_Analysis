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

#One way to open a file
#election_data = open(file_to_load,'r')
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Get the headers
    headers = next(file_reader)
    print(headers)

with open(file_to_save, 'w') as txt_file:
    txt_file.write('Counties in the Election\n')
    txt_file.write('------------------------\n')
    txt_file.write('Arapahoe\nDenver\nJefferson')





#Do stuff

# Close the file
# If we use with, the following line is not needed
# election_data.close()



