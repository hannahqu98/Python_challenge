import os
import csv

budgetdata_csv = os.path.join( "resources", "budget_data.csv")
output_path =os.path.join("..","anaysis","PyBank.csv")

total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0
prev_net = 0 

with open(budgetdata_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
       
       total_months += 1
       total_net += int(row[1])
      
       net_change = int(row[1]) - prev_net
       prev_net = int(row[1])
       net_change_list += [net_change]
       month_of_change += [row[0]]
       
       if net_change > greatest_increase[1]:
           greatest_increase[0] = row[0]
           greatest_increase[1] = net_change
       
       if net_change < greatest_decrease[1]:
           greatest_decrease[0] = row[0]
           greatest_decrease[1] = net_change

net_monthly_avg = sum(net_change_list) / len(net_change_list)

output = (
   f"Financial Analysis\n"
   f"----------------------------\n"
   f"Total Months: {total_months}\n"
   f"Total: ${total_net}\n"
   f"Average  Change: ${net_monthly_avg:.2f}\n"
   f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
   f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output) 

output_path =os.path.join("analysis","PyBank.csv")

with open(output_path) as datafile :
    writer = csv.write(output)


