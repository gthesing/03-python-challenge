import os
import csv
import subprocess

path = os.path.join("../Resources/budget_data.csv")

months = 0              # keeps track of the number of rows
profit = 0              # keeps track of net profit
g_profit = 0            # amount for greatest increase in profit
g_loss = 0              # amount for greatest decrease in profit
g_profit_date = ''      # month of greatest profit increase
g_loss_date = ''        # month of greatest profit decrease

with open(path, newline = '') as BudgetData:
    csvreader = csv.reader(BudgetData, delimiter=',')
    for row in enumerate(csvreader):
        if row[0] == 0:
            header = row
            # print(f'\nHeader: {header}')      # Useful while making edits
        else:
            item = row[1]
            date = item[0]
            pro = float(item[1])
            # print(f'Profit/Loss was {pro} for {date}')    # Useful for editing
            months = months + 1
            profit = profit + (pro)

            if pro > g_profit: 
                g_profit = pro
                g_profit_date = date
            if pro < g_loss:
                g_loss = pro
                g_loss_date = date

average_change = round(profit/months,2)

print(f'\nFinancial Analysis \n---------------------------------------------------------')
print(f'Total Months: {months}')
print(f'Total: ${profit}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {g_profit_date} ({g_profit})')
print(f'Greatest Decrease in Profits: {g_loss_date} ({g_loss})')
print('---------------------------------------------------------')



""" # froze the terminal so probably outdated...
with open("PyBank.txt", "w") as output:
    subprocess.call(["python", "/main.py" ], stdout=output)
"""