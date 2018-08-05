import csv
import os
from collections import Counter

path = os.path.join("Resources","election_data.csv")

voter = []
county = []
candidate = []

with open(path,newline="") as infile:
    csv = csv.reader(infile ,delimiter = ",")
    next(csv, None)
    for row in csv :
        voter.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

voter_count = 0

for i in voter :
    voter_count += 1

candidate_count = Counter(candidate)

candidate_print = []

for k, v in candidate_count.items() :
    candidate_print.append((f"{k}: {(v/voter_count*100):.2f}% ({v})"))

printout=('\n'.join(candidate_print))

value = 0
key = ""

for k, v in candidate_count.items() :
    if v == 0 :
        value = v
        key = k
    elif v > value :
        value = v
        key = k
final = (
    f"Election Results\n"
    f"-------------------\n"
    f"Total Votes: {voter_count}\n"
    f"-------------------\n"
    f"{printout}\n"
    f"-------------------\n"
    f"Winner: {key}\n"
    f"-------------------\n")
print(final)

with open("Output.txt", "w") as outfile:
    outfile.write(final)