#Use election_data.csv as dataset. Column A Voter ID 
# column B County, Column C Candidate

#import os module
import os

#import csv module to be able to read csv file
import csv

#store the file path in a variable
poll = os.path.join('Resources','election_data.csv')

#open the file in read mode
with open(poll) as csv_file:
    #specify delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter= ',')
    #read header row first
    csv_header = next(csv_file)

    #set vote counter at 0
    votecount = 0
    #create list to store candidate names
    candidate_list = []
    #create list to store votes for each candidate
    votes_list = []
    #store votes for first candidate
    votes1 = 0
    #store votes for second candidate
    votes2 = 0
    #store votes for third candidate
    votes3 = 0
    #create list to store percentage of votes won by each candidate
    percent_list = []
    #store percentage won by first candidate
    percent1 = 0
    #store percentage won by second candidate
    percent2 = 0
    #store percentage won by third candidate
    percent3 = 0

    #read each row in csv after header
    for row in csv_reader:
        #count all rows to obtain total number of votes
        votecount +=1
        #set candidate name as value in Column C
        candidate = row[2]
        
        #if the candidate name in this row is not in the candidate list, store name in candidate list
        if candidate not in candidate_list:
            candidate_list = candidate_list + [candidate]
        
        #if candidate name in the row is equal to first candidate name...
        if row[2] == candidate_list[0]:
            #add 1 to count of votes for first candidate
            votes1 += 1
        #if candidate name in the row is equal to second candidate name...
        elif row[2] == candidate_list[1]:
            #add 1 to count of votes for second candidate
            votes2 += 1
        #if candidate name in the row is equal to third candidate name...
        else:
            #add 1 to count of votes for third candidate
            votes3 += 1
    
    #add votes for first candidate to list of votes
    votes_list = votes_list + [votes1]
    #add votes for second candidate to list of votes
    votes_list = votes_list + [votes2]
    #add votes for third candidate to list of votes
    votes_list = votes_list + [votes3]
    
    #calculate percentage of total votes received by first candidate
    percent1 = (votes1/votecount)*100
    #add percentage of votes to list of obtained percentages
    percent_list = percent_list + [round(percent1,3)]

    #calculate percentage of total votes received by second candidate
    percent2 = (votes2/votecount)*100
    #add percentage of votes to list of obtained percentages
    percent_list = percent_list + [round(percent2,3)]

    #calculate percentage of total votes received by third candidate
    percent3 = (votes3/votecount)*100
    #add percentage of votes to list of obtained percentages
    percent_list = percent_list + [round(percent3,3)]

#if votes received by first candidate is the maximum in the votes list...
if votes_list[0] == max(votes_list):
    #then first candidate is the winner
    winner = candidate_list[0]
#if votes received by second candidate is the maximum in the votes list...
elif votes_list[1] == max(votes_list):
    #then second candidate is the winner
    winner = candidate_list[1]
#if votes received by third candidate is the maximum in the votes list...
else:
    #then third candidate is the winner
    winner = candidate_list[2]

    
#output summary of total votecount, candidate names, candidate percentages, candidate votes, and winner
print('Election Results')
print('--------------------------------')
print(f'Total Votes: {votecount}')
print('--------------------------------')
print(f'{candidate_list[0]}: {percent_list[0]}% ({votes_list[0]})')
print(f'{candidate_list[1]}: {percent_list[1]}% ({votes_list[1]})')
print(f'{candidate_list[2]}: {percent_list[2]}% ({votes_list[2]})')
print('--------------------------------')
print(f'Winner: {winner}')
print('--------------------------------')

#create analysis summary file and save in analysis folder
analysis = os.path.join('Analysis','analysis.txt')

#open analysis file in write mode
with open(analysis, 'w') as text_file:
    #write summary on analysis file
    text_file.write(f'''Election Results
--------------------------------
Total Votes: {votecount}
--------------------------------
{candidate_list[0]}: {percent_list[0]}% ({votes_list[0]})
{candidate_list[1]}: {percent_list[1]}% ({votes_list[1]})
{candidate_list[2]}: {percent_list[2]}% ({votes_list[2]})
--------------------------------
Winner: {winner}
--------------------------------
''')
    #close analysis file
    text_file.close()