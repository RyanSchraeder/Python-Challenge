import os
import csv

#Define file path
electiondatafile = os.path.join('election_data.csv')

def totals (voteDataRow):
            
    # find the votes row
    totalVotesRow = int(voteDataRow[0])

    # set total vote percent
    totalVotesPercent = int(voteDataRow[0])/totalVotesRow

    #   make a dictionary storing candidate data and votes within the loop
    candidate = voteDataRow[2]
    
#Read in the csvfile
with open('electiondatacsv', 'r') as electiondatafile:
    #split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    #create the loop
for totalVotesRow in CandidatesDictionary():
    
    print("Election Results: ")
    print("--------------------------")
    print(f"Total Votes: {totalVotesRow}")
    print("--------------------------")
    print(CandidatesDictionary)
    print("--------------------------")
    print(f"Winner: {candidate if totalVotesPercent > 50}")
    print("--------------------------")

#Write the csvfile as a txt
with open('electiondatacsv', 'w') as electiondatafile
    csvwriter = csv.writer(electiondatafile, delimiter=",")