import os
import csv

# current_directory = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join("PyPoll","Resources", "election_data.csv")

# Open the file using "read" mode. Specify the variable to hold the contents
with open(output_path, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Define variables used
    vote_count = 0
    candidates ={}
    winner = []

    #Loop through each row, excluding the head in the CSV file,
    #counting the number of votes and unique canidates

    for row in csvreader:
        vote_count+=1
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] +=1
    
    # Find the winner based off the highest tally of votes

    for items in candidates:

        if len(winner) == 0:
            winner.append(items)
            winner.append(candidates[items])
        elif winner[1] < candidates[items]:
            winner[0] = items
            winner[1] = candidates[items]
        else:
            continue

    # Print the results
    
    print('\n\n\nElection Results\n\n---------------------------')
    print(f'\nTotal Votes: {vote_count}\n')
    print('---------------------------\n')
    for keys in candidates:
        print(f'{keys}: {round((candidates[keys]/vote_count)*100,3)}% ({candidates[keys]})\n')
    print('---------------------------\n')    
    print(f'Winner : {winner[0]}\n')
    print('---------------------------\n')   

# Write the information to a txt file

output_path = os.path.join("PyPoll","analysis", "election_output.txt")
with open(output_path,'w') as file:
    file.write('\n\n\nElection Results\n\n---------------------------')
    file.write(f'\nTotal Votes: {vote_count}\n')
    file.write('---------------------------\n')
    for keys in candidates:
        file.write(f'{keys}: {round((candidates[keys]/vote_count)*100,3)}% ({candidates[keys]})\n')
    file.write('---------------------------\n')    
    file.write(f'Winner : {winner[0]}\n')
    file.write('---------------------------\n')   
