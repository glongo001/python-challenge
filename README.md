# Python-challenge

This challenge is divided into two parts, the first part is PyBank and the second part is PyPoll

PyBank
A file containing budget data was analyzed to obtain:

    The total number of months in the dataset
        This was obtained by counting the number of rows, each row represented one month in the dataset
    The total amount of "Profits/Losses" over time
        Obtained by adding all values in the "Profits/Losses" column
    The changes in "Profits/Losses" month to month during the entire period
        Obtained by subtracting the "Profits/Losses" in the previous row from the profits losses in the current row
    The average change in "Profits/Losses"
        Obtained by storing all changes in a list, adding the values in the list and dividing them by the number of elements in the list
    The greatest increase in profits
        Looked for the maximum increase in profits in the changes list
    The greatest losses
        Looked for the maximum decrease in profits in the changes list

PyPoll
A file containing election data was analyzed to obtain:

    The total number of votes cast
        Obtained by counting the number of rows, each row represented one vote in the dataset
    A list of candidates who received votes
        Stored the candidate names in a list
    The percentage of votes each candidate received
        Obtained the percentage based on the number of votes each candidate received and the total number of votes
    The number of votes each candidate received
        Counted the number of rows in which each candidate name appeared
    The winner of the election
        Looked for the maximum number of votes in the votes list
