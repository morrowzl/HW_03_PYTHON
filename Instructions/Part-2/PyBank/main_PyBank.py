#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#
#
#As an example, your analysis should look similar to the one below:
#
#
#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)

# -*- coding: UTF-8 -*-
"""PyBank Homework Solution."""

# Dependencies
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("budget_analysis.txt")

# Track various financial parameters
monthly_changes = []
net_change = 0
previous_net = 0
net_change_list = []
total = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999]

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    
    header = next(reader)
    
    for row in reader:
    
        monthly_changes.append(
                {'period': str(row[0]), 'change': int(row[1])})
        total_months = int(len(monthly_changes))
        change = (int(row[1]))
        net_change = change - previous_net
        previous_net = change
        net_change_list.append(net_change)
        total += change
        increase = int(greatest_increase[1])
        decrease = int(greatest_decrease[1])
        change = int(row[1])
        
        if change > increase:
            greatest_increase[0] = (row[0])
            greatest_increase[1] = (row[1])
            
        elif change < decrease:
            greatest_decrease[0] = (row[0])
            greatest_decrease[1] = (row[1])
            
        average_change = (sum(net_change_list))/(len(net_change_list))
        
        
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total}\n"
    f"Average  Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)

with open(file_to_output, "w") as text_file:
    print(output, file=text_file)   
    