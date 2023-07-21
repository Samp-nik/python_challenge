import os
import csv

output_path = os.path.join("PyBank","Resources", "budget_data.csv")

# Open the file using "read" mode. Specify the variable to hold the contents
with open(output_path, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    # Define variables used

    date_count = 0
    total_net_income = 0
    profit_lst = []
    change_profit = []
    change_date = dict()

    #Loop through each row, excluding the head in the CSV file,
    #counting the number of dates and summing the values

    for row in csvreader:
        date_count +=1
        total_net_income += int(row[1])
        profit_lst.append(int(row[1]))
        if date_count > 1:
            change_profit.append(profit_lst[date_count-1] - profit_lst[date_count-2])
            change_date[profit_lst[date_count-1] - profit_lst[date_count-2]] = row[0]

    # Print the results in terminal

    print('\n\n\nFinancial Analysis\n\n---------------------------')
    print(f'\nTotal Months: {date_count}\n')
    print(f'Total: ${total_net_income}\n')
    print(f'Total Change: ${sum(change_profit)}\n')
    print(f'Average Change: ${round(sum(change_profit)/(date_count -1),2)}\n')
    print(f'Greatest Increase in Profits: {change_date[(max(change_profit))]}  $({max(change_profit)})\n')
    print(f'Greatest Decrease in Profits: {change_date[(min(change_profit))]}  $({min(change_profit)})\n')

# Write the results to a txt file

output_path = os.path.join("PyBank","analysis", "budget_output.txt")
with open(output_path,'w') as file:
    file.write('\n\n\nFinancial Analysis\n\n---------------------------')
    file.write(f'\n\nTotal Months: {date_count}\n\n')
    file.write(f'Total: ${total_net_income}\n\n')
    file.write(f'Total Change: ${sum(change_profit)}\n\n')
    file.write(f'Average Change: ${round(sum(change_profit)/(date_count -1),2)}\n\n')
    file.write(f'Greatest Increase in Profits: {change_date[(max(change_profit))]}  (${max(change_profit)})\n\n')
    file.write(f'Greatest Decrease in Profits: {change_date[(min(change_profit))]}  (${min(change_profit)})\n')

   