import os
import csv

path = os.path.join("../Resources/election_data.csv")

total_votes = 0
d = {}

with open(path, newline = '') as ElectionData:
    csvreader = csv.reader(ElectionData, delimiter=',')
    for row in enumerate(csvreader):
        if row[0] == 0:
            header = row
        else:
            total_votes = total_votes + 1
            info = row[1]
            choice = info[2]
            if choice in d:
                d[choice] = d[choice] + 1
            else:
                d[choice] = 1

winner = ''
votes_winner = 0

### OUTPUT ###
print(f'\nElection Results')
print('---------------------------')
print(f'Total Votes: {total_votes}')
print('---------------------------')
for key, value in d.items():
    votes = value
    percent = float(100 * (votes / total_votes))
    percent = round(percent, 4)
    print(f'{key}: {percent}% ({value})')
    #print(key + ': ' + '{:.3%}'.format(percent) + ' ('votes')')
    if votes > votes_winner:
        votes_winner = votes
        winner = key
print('---------------------------')
print(f'Winner: {winner}')
print('---------------------------')
