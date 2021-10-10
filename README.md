# Election_Analysis
## Project Overview

### Purpose
The Colorado Board of Elections is asking for a vote count report in a recent election. The information that they need is:

1. Total number of votes cast
2. The voter turnout for each county
3. The percentage of votes from each county out of the total count
4. The county with the highest turnout
5. A complete list of candidates who received votes
6. Total number of votes each candidate received
7. Percentage of votes each candidate won 
8. The winner of the election based on popular vote 


### Background
An election audit is needed in the tabulated results for the US congressional precinct in Colorado. The process should be automated so it can be used in congressional districs, senatorial districts and local elections.

## Resources
- Data source: election_results.csv
- Software: Python 3.9.7, Visual Studio Code 1.61.0
- Data output: election_results.txt 

## Analysis
The analysis of the elections shows that:
- There was a total of 369,711 votes in the Colorado elections. 
- There were 3 counties involved in the election, with the following votes distribution:
  - Jefferson County with 10.5% (38,855) of the votes
  - Denver County with 82.8% (306,055) of the votes
  - Arapahoe County with 6.7% (24,801) of the votes
- There were 3 candidates in the election, with the folloing votes distribution:
  - Charles Casper Stockham with 23.0% (85,213) of the votes
  - Diana DeGette with 73.8% (272,892) of the votes
  - Raymon Anthony Doane with 3.1% (11,606) of the votes
 
 ### Results
 The election results are:
 - The highest county turnout was Denver County, with a 82.8% of the votes and a total of 306,055 votes.
 - The winner of the election was Diana DeGette, with a 73.8% of the votes and a total of 272,892 votes.

## Summary
The script can be used to automate the process of counting the votes. It doesn't matter the number of counties or candidates involved in the election, it will deliver the highest county turnout and the winner of the election. So, is repeatable and scalable and can be used in congressional districs, senatorial districts and local elections.

Additional functions that can be added in the future are:
- The candidate vote distribution for each county. 
- And a little more complex, vote participation by county. For this, is required to get the total population of each county. 

