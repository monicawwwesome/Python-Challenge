# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

  # The total number of votes cast

  #* A complete list of candidates who received votes

  # The percentage of votes each candidate won

  #* The total number of votes each candidate won

  #* The winner of the election based on popular vote.

#* As an example, your analysis should look similar to the one below:

  #```text
  #Election Results
  #-------------------------
  #Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
  #-------------------------
  #```


#Read csv file
import os
import csv

election_data = os.path.join('PyPoll','Resources','election_data.csv')
with open(election_data) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  
  #Skip headers
  csv_header = next(csvreader, None)

  voter = []
  khan = 0
  correy = 0
  li = 0
  otooley = 0
  
  for row in csvreader:

    #Append voter information
    voter.append(row[0])
    total_votes = len(voter)

    #Calculate the vote each candidate got
    if row[2] == "Khan":
      khan += 1
    elif row[2] == "Correy":
      correy += 1
    elif row[2] == "Li":
      li += 1
    elif row[2] == "O'Tooley":
      otooley += 1
#Create dictionary to find the winner
candidates_list = ["Khan","Correy","Li","O'Tooley"]
votes = [khan, correy, li, otooley]
vote_dict = {candidates_list[i]:votes[i] for i in range (len(votes))}
winner = max(vote_dict, key=vote_dict.get)


#Calculate percentage
khan_pct = khan/total_votes*100
correy_pct = correy/total_votes*100
li_pct = li/total_votes*100
otooley_pct = otooley/total_votes*100


print("Election Results")
print("-------------------------") 
print("Total Votes: " + str(total_votes))
print("-------------------------")
print(f"Khan: {khan_pct:.3f}% ({khan})")
print(f"Correy: {correy_pct:.3f}% ({correy})")
print(f"Li: {li_pct:.3f}% ({li})")
print(f"O'Tooley: {otooley_pct:.3f}% ({otooley})")
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")


    