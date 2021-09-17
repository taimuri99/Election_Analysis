# Election Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election. 

1) Calculate the total number of votes cast.
2) Get a complete list of candidates who received votes.
3) Calculate the total number of votes each candidate recieved.
4) Calculate the percentage of votes each candidate won.
5) Determine the winner of the election based on popular vote.

## Resources

- Data Source: election_results.csv
- Software: Python 3.8.5, Visual Studio Code, 1.38.1

## Summary
The analysis of the election result shows that:
- There were 369,711 votes cast in the election.
- The counties were:
  - Jefferson
  - Denver
  - Arapahoe
- The county results were:
  - Jefferson county had "10.5%" of the vote with "38,855" votes.
  - Denver county had "82.8%" of the vote with "306,055" votes.
  - Arapahoe county had "6.7%" of the vote with "24,801" votes.
- The county with the largest turnout was:
  - Denver County, which had "82.8%" of the vote with "306,055" votes.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate result were:
  - Charles Casper Stockham received "23.0%" of the vote and "85,213" number of votes.
  - Diana DeGette received "73.8%" of the vote and "272,892" number of votes.
  - Raymon Anthony Doane received "3.1%" of the vote and "11,606" number of votes.
- The winner of the election was:
  - Diana DeGette, who recieved "73.8%" of the vote and "272,892" number of votes.

## Challenge Overview
For this challenge, in addition to calculating the winner from each of the candidates with their vote count and percentage, we were also tasked to calculate the voter turnout and voter turnout percentage of the three counties. Reading the CSV file with the data of the three counties and candidates, the python script calculated the additional requirements that were:
1) The voter turnout for each county.
2) The percentage of votes from each county out of the total count.
3) The county with the highest turnout.

The python script written in Module 3 was changed to include county vote and county vote percentage and resulted in an output in text file with all these results.

<img width="308" alt="Output Result" src="https://user-images.githubusercontent.com/87828174/133713251-ff11446a-4d88-4543-acee-7ed0e9169ab9.png">

## Challenge Summary
### Election Audit Results
#### Deliverable 1
This required us to output the county perfomance results to the terminal. We first initialised a list for county options and a dictionary for counties and their votes while also initialising the total votes to 0. The largest county turnout count and string to hold its name was also set in the beginning. 

<img width="428" alt="CountyInitialised" src="https://user-images.githubusercontent.com/87828174/133714531-720036e2-b836-4c9c-8c65-1d89b0e4d9c5.png">

The following code, very similar to calculating candidate vote and vote share of the total, calculates the county perfomance. The CSV file is read using:

    with open(file_to_load) as election_data:
      reader = csv.reader(election_data)

Iterating through the rows using a for-loop, total votes are incremented, candidate name is extracted from row of column 2 and county name is extracted from column 1. For each row, the county name is appended to the list of county options if not already present. The value of vote counts belonging to the county name keys in the dictionary are increased for each vote in that county. The following code shows how this was done:

<img width="536" alt="CountyPerformanceUodatedwithReadingFile" src="https://user-images.githubusercontent.com/87828174/133715343-3d653a58-4592-4fac-a0ec-4ddb25bc6e96.png">

After going through the rows and updating the information on county performance, a for-loop was created to get the county from the county-vote dictionary. The county vote percentage was calculated from the total vote. An if statement calculated the largest turnout and set the county name and county vote count to the empty variables initialised in the beginning. The following code shows this:

<img width="707" alt="CountyPerformanceCode" src="https://user-images.githubusercontent.com/87828174/133714311-4a772ff2-a468-4c49-8dee-526989f890ce.png">

#### Deliverable 2
The second deliverable required us to output the result to a text file which had a directory pathway set in the beginning of the script. After importing the csv and os module, the following code was added to create a directory path to write to a text file and read a csv file:

    file_to_load = os.path.join("Resources", "election_results.csv")
    file_to_save = os.path.join("Analysis", "election_analysis.txt")
    
The text file was opened with an option to write:

    with open(file_to_save, "w") as txt_file:
    
A series of f statements were written which were then written to the text file:

    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        #f"Largest County Count: {largest_county_count:,}\n"
        f"-------------------------\n")
    print(winning_county_summary)
    txt_file.write(winning_county_summary)
    
and:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)

This code after being run, results in the output text file as shown in the Challenge Overview section.

### Election Audit Summary
The script designed for this challenge can work for any type of election.
1) If there is a different csv file, the variable to load a file using the directory path can be changed to the different csv file and therefore it would load the different csv file with a different data set.

Since the candidate options, candidate votes, county options and county votes are both lists and dictionaries which can be appended with any number of candidates or counties, it will read and store the performance for different people and counties as well. The only other change one could make is:

2) If the candidate and county data are in different columns of a csv file and not in the ones for the csv file we used for this challenge, the following code can be changed to accommodate:

        for row in reader:
          candidate_name = row[a]
          county_name = row[b]
 
 Where a and b are the index of the columns which hold the necessary information.
        
   



