import os
import csv


from sniffio import current_async_library

budgetdata_csv = os.path.join( "..","resources", "budget_data.csv")

output_csv = os.path.join( "..","analysis", "budget_analysis.txt")

total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0

with open(budgetdata_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader,None)

    for row in csvreader:
       
       total_months += 1
       total_net += int(row[1])

        #count+= 1

        #current= int(row[1])
        #total += current 
       # Track the net change
       net_change = int(row[1]) - prev_net
       prev_net = int(row[1])
       net_change_list += [net_change]
       month_of_change += [row[0]]
       # Calculate the greatest increase
       if net_change > greatest_increase[1]:
           greatest_increase[0] = row[0]
           greatest_increase[1] = net_change
       # Calculate the greatest decrease
       if net_change < greatest_decrease[1]:
           greatest_decrease[0] = row[0]
           greatest_decrease[1] = net_change
# Calculate the Average Net Change
    net_monthly_avg = sum(net_change_list) / len(net_change_list)
# Generate Output Summary
output = (
   f"Financial Analysis\n"
   f"----------------------------\n"
   f"Total Months: {total_months}\n"
   f"Total: ${total_net}\n"
   f"Average  Change: ${net_monthly_avg:.2f}\n"
   f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
   f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)

    #for row in csvreader:
        #count+= 1

        #current= int(row[1])
        #total += current 
         
        #if count > 1:
            #changes.append(previous - current)
        
        #previous = current


    #max_value = max(changes)
    #min_value = min(changes)

    #max_month = changes.index(max_value) + 1
    #min_month = changes.index(min_value) + 1

      
#print("Total Months: " + str(count))

#print("Total: $" + str(total))

#print("Average Change: " + str(sum(changes)/len(changes)))

#print("Greatest Increase in Profits: " + str(changes[max_month]) + str(max_value))



    #csvreader = csv.reader(csvfile, delimiter=",")

    #print("Financial Analysis")
    #print("------------------------------------------------------------")

    #csv_header = next(csvreader,None)

    #Total_months = len(date)
    #print("Total months : " + Total_months)
