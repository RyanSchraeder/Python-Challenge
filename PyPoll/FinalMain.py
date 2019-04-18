import os
import csv 

electiondatafile = os.path.join('election_data_short.csv')
file_to_output = os.path.join('analysis.txt')

total_votes_count = 0 

candidate_list = []
candidate_votes_dict = {}
candidate_winner = ""
candidate_winner_vote_count = 0 


with open(electiondatafile, 'r') as electiondata:
    #split the data on commas
    csvreader = csv.reader(electiondata, delimiter=',')
    header = next(csvreader)
    print(header)
    
    for row in csvreader:
        total_votes_count = total_votes_count + 1
        print(total_votes_count)
        print(row)
        candidate_row = row[2]
        print(candidate_row)
        
        if candidate_row not in candidate_list:
            candidate_list.append(candidate_row)
            candidate_votes_dict [candidate_row] = 0
            print(candidate_list)
            print(candidate_votes_dict)

        candidate_votes_dict[candidate_row] = candidate_votes_dict[candidate_row] + 1
        print(candidate_votes_dict)

print (candidate_list)
print (candidate_votes_dict)

with open(file_to_output, "w") as txt_file:
    
# Print the final vote count (to bash)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"-
        f"Total Votes: {total_votes_count}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    
    for candidate in candidate_votes_dict: 
        candidate_vote = candidate_votes_dict.get(candidate)
        print(candidate_vote)
        vote_pct = (candidate_vote / total_votes_count) * 100

        if candidate_vote > candidate_winner_vote_count:
            candidate_winner_vote_count = candidate_vote
            candidate_winner = candidate
        
        voter_output = f"{candidate}: {vote_pct:.3f}% ({candidate_vote})\n"
        print(voter_output, end="")

       # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

