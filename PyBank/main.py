import csv
import os
# Read the financial data from the CSV file
csvpath = os.path.join("C:\\Users\\gbegn\\python_challege\\PyBank\\Resources\\budget_data.csv")
output_file = os.path.join("C:\\Users\\gbegn\\python_challege\PyBank\analysis\budget_analysis.txt")


total_months = 0
net_total = 0
changes = []
dates = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_months += 1
        net_total += int(row[1])
        if dates:
            changes.append(int(row[1]) - prev_profit_loss)
        dates.append(row[0])
        prev_profit_loss = int(row[1])

average_change = sum(changes) / len(changes)
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Find corresponding dates for greatest increase and decrease
increase_date = dates[changes.index(greatest_increase) + 1]
decrease_date = dates[changes.index(greatest_decrease) + 1]

# Print and export results
output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {increase_date} (${greatest_increase})
Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})
"""

print(output)

with open("analysis", "w") as output_file:
    output_file.write(output)
       