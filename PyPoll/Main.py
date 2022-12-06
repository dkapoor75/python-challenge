# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # defining variables
    votecount = 0
    unique_candidate = []
    candidate_votes = {}
    winner_count = 0
    winning_candidate = ""

    for row in csvreader:
        
        # calculate the total votes
        votecount = votecount + 1
                
        # if the voters is not in the unique_candidate list then add it there
        # and also add the record for this candidate in the candidate_votes dictionary which will contain candidates total votes
        if row[2] not in unique_candidate:
           unique_candidate.append(row[2])
           candidate_votes[row[2]] = 1
        else:
           candidate_votes[row[2]] = candidate_votes[row[2]] + 1

    
    # Printing to the Terminal

    print(f"Election Results")
    print(" ")
    print(f"----------------------------")
    print(" ")
    print(f"Total Votes: {votecount}")
    print(" ")
    print(f"----------------------------")
    print(" ")

    # finding out the winning candidate

    for x in candidate_votes:

        votes = candidate_votes[x]
        votes_percentage = ( votes / votecount )* 100

        print(f"{x} : {votes_percentage:.3f}% ({votes})")       
        print(" ")

        if votes > winner_count:
           winner_count = votes 
           winning_candidate = x

    # Printing to the Terminal

    print(" ")
    print(f"----------------------------")
    print(" ")
    print(f"Winner: {winning_candidate}")
    print(" ")
    print(f"----------------------------")
    print(" ")
    
    # Creating a new text file in analysis folder

    Textfilepath = os.path.join("Analysis", "analysis.txt")
    f = open(Textfilepath, "x")

    # defining the path
    textfilepath = os.path.join("Analysis", "analysis.txt")

    # creating the text file with write attribute
    textfile = open(Textfilepath, "w")

    # writing to text file

    textfile.write("Election Results \n")
    textfile.write("  \n")
    textfile.write(f"---------------------------- \n")
    textfile.write("  \n")
    textfile.write(f"Total Votes: {votecount} \n")
    textfile.write("  \n")
    textfile.write(f"---------------------------- \n")
    textfile.write("  \n")

    # finding out the winning candidate

    for x in candidate_votes:

        votes = candidate_votes[x]
        votes_percentage = ( votes / votecount )* 100

        # writing to text file

        textfile.write(f"{x} : {votes_percentage:.3f}% ({votes}) \n")
        textfile.write("  \n")

        if votes > winner_count:
           winner_count = votes 
           winning_candidate = x

    # writing to text file

    textfile.write("  \n")
    textfile.write(f"---------------------------- \n")
    textfile.write("  \n")
    textfile.write(f"Winner: {winning_candidate} \n")
    textfile.write("  \n")
    textfile.write(f"---------------------------- \n")
    textfile.write("  \n")
    