'''Use election_data.csv as dataset. Column A Voter ID
column B County, Column C Candidate. Calculate:
- total number of votes cast
- list of candidates who received votes
- percentage of votes each candidate won
- total number of votes each candidate won
- winner of election popular vote'
- export to text file'''

#import os module
import os

#import csv module to be able to read csv file
import csv

#store the file path in a variable
budget = os.path.join('Resources','budget_data.csv')

#open the file in read mode
with open(budget) as csv_file:
    #specify delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter= ',')
    #read header row first
    csv_header = next(csv_file)

    votecount = 0
    candidate_list = []
    candidate_votes = 0
    candidate_percent = 0
    for row in csv_reader:
        votecount +=1
        if row[2] <> row[2]:





print('Election Results')
print('--------------------------------')
print(f'Total Votes: {votecount}')
print('--------------------------------')
print(f'name12and3, percent, number')
print('--------------------------------')
print('Winner: ')
print('--------------------------------')