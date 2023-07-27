# Python-challenge
This challenge is divided into two parts, the first part is PyBank and the second part is PyPoll

## PyBank
I created a Python script that analyzes the financial records of a company.

1. First, I imported the dataset named `budget_data.csv`, the dataset contained the columns `Date` and `Profit/Losses`.

2. I calculated the total number of months in the dataset by setting `monthcount` to 0 and counting the number of rows after the header.

3. I calculated the net total amount of `Profit/Losses` over the entire period by setting `total` to 0 and adding the values in each row.

4. I calculated the changes in `Profit/Losses` over the entire period by storing the month and difference in `Profit/Losses` between two consecutive rows in a list, and calculated the average of those changes by adding all values in the list and dividing it by the number of items in the list.

5. I calculated the greatest increase in profits by comparing all changes in profits between consecutive rows and stored the largest value in `increase`.

6. I calculated the greatest decrease in profits by comparing all changes in profits between consecutive rows and stored the smallest value in `decrease`.

7. Then, I created a text file with Python and stored the total number of months in the dataset, the total amount of "Profits/Losses" over time, the changes in "Profits/Losses" month to month during the entire period, the average change in "Profits/Losses", the greatest increase in profits, and the greatest decrease in profits.

![alt text](https://github.com/glongo001/python-challenge/blob/main/PyBank/Analysis/PyBank_analysis.png)

## PyPoll
I created a Python script that analyzes election data from a small rural town.

1. First, I imported the dataset named `election_data.csv`, the dataset contained the columns `Voter ID`, `County`, and `Candidate`.

2. I calculated the total number of votes cast by setting `votecount` to 0 and counting the number of rows after the header.

3. I created a list that stored the names of all the candidates that received votes.

4. I obtained the total number of votes each candidate won by setting a counter for the votes cast for each candidate and stored the totals in a list.

5. I obtained the percentage of votes each candidate won by dividing the number of votes each candidate received by the total votecount and multiplied the result by 100, and stored the percentages in a list.

6. Then, I created a text file with Python and stored the total number of votes cast, the list of candidates who received votes, the percentage of votes each candidate received, the number of votes each candidate received, and the winner of the election.

![alt text](https://github.com/glongo001/python-challenge/blob/main/PyPoll/Analysis/PyPoll_analysis.png)