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
current = 0
previous = 0
change = 0
delta = 0

with open(path, newline = '') as BudgetData:
    csvreader = csv.reader(BudgetData, delimiter=',')
    for row in enumerate(csvreader):
        if row[0] == 0:
            header = row
            # print(f'\nHeader: {header}')      # Useful while making edits
        else:
            item = row[1]
            date = item[0]
            current = float(item[1])
            # print(f'Profit/Loss was {pro} for {date}')    # Useful for editing
            months = months + 1
            profit = profit + current
            delta = current - previous

            if row[0] == 1:         
                change = 0         
            else:
                change = change + (current - previous)

            if delta > g_profit:
                g_profit = delta
                g_profit_date = date
            if delta < g_loss:
                g_loss = delta
                g_loss_date = date

        previous = current

average_change = round(change/(months-1), 2)

print(f'\nFinancial Analysis \n---------------------------------------------------------')
print(f'Total Months: {months}')
print(f'Total: ${profit}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {g_profit_date} (${g_profit})')
print(f'Greatest Decrease in Profits: {g_loss_date} (${g_loss})')
print('---------------------------------------------------------')


 
with open("PyBank.txt", "w") as output:
    subprocess.call(["python", "main.py" ], stdout=output)

   #^this works when I Ctrl+C out of the
   # program for some reason???

