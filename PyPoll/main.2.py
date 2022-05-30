import os
import csv

election_data_csv = os.path.join("resources","election_data.csv")

khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
total_vote = 0 

with open(election_data_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        

        if row[2] == "Khan" :
            khan_votes += 1 
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        elif row[2] == "O'Tooley":
            otooley_votes += 1

total_votes = khan_votes + correy_votes + li_votes + otooley_votes


candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]
    
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)


khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

output = f"Election Results\n"
f"----------------------------\n"
f"Total Votes: {total_votes}\n"
f"----------------------------\n"
f"Khan: {khan_percent:.3f}% ({khan_votes})\n"
f"Correy: {correy_percent:.3f}% ({correy_votes})\n"
f"Li: {li_percent:.3f}% ({li_votes})\n"
f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})\n"
f"----------------------------\n"
f"Winner: {key}\n"
f"----------------------------\n"


print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

file_name ="pypoll.txt"
text_file = open("analysis/pypoll.txt","w")
text_file.write(output)
text_file.close()
    



