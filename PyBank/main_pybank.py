import os
import csv

path = os.path.join("Resources","budget_data.csv")

months = []
revenue = []

with open(path,newline="") as infile:
    csv = csv.reader(infile ,delimiter = ",")
    next(csv)
    for row in csv :
        months.append(row[0])
        revenue.append(int(row[1]))

count_months = 0

for i in months :
    count_months += 1

sum_revenue = round(sum(revenue),2)

zipped = zip(revenue[:-1], revenue[1:])

def change(x,y) :
    return y - x
    

changes = list(map(change, revenue[:-1],revenue[1:]))

total_avg=round((sum(changes)/len(changes)),2

max_change = max(changes)

max_month = months[list(changes).index(max_change) + 1]

min_change = min(changes)

min_month = months[list(changes).index(min_change) + 1]

final = (f"Financial Analysis\n"
    f"----------------------\n"
    f"Total Months: {count_months}\n"
    f"Total: $ {sum_revenue}\n"
    f"Average Change: $ {total_avg}\n"
    f"Greatest Increase in Profits: {max_month} (${max_change})\n"
    f"Greates Decrease in Profits: {min_month} (${min_change})\n")

print(final)

with open("Output.txt", "w") as outfile:
    outfile.write(final)