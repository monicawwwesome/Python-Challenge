#Read csv file
import os
import csv

budget_data = os.path.join('PyBank','Resources','budget_data.csv')
with open(budget_data) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  
  #Skip headers
  csv_header = next(csvreader, None)
  
  months = []
  profit = []

  for row in csvreader:  
    #Append months and profit/loss
    months.append(str(row[0]))
    profit.append(int(row[1]))

    #Calculate profit change between months
    change = []
    for i in range(len(profit)-1):
      change.append(profit[i+1] - profit[i])
      avg_change = sum(change) / len(change)
      avg_change = round(avg_change,2)

  #Output Analysis
  print("Financial Analysis") 
  print("----------------------------")
  print("Total Months: " + str(len(months)))
  print("Total: $" + str(sum(profit)))
  print("Average Change: $" + str(avg_change))
  print("Greatest Increase in Profits: $" + str(max(change)))
  print("Greatest Decrease in Profits: $" + str(min(change)))







  
