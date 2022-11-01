#use budget_data.csv with column A as Date and column B as Profit/Losses

#import os module to store file path in a variable
import os
#import csv module to be able to read and work with the csv file
import csv
#store the file path in budget variable
budget = os.path.join('Resources','budget_data.csv')

#open the file as csv_file
with open(budget) as csv_file:
    #specify delimiter and variable that holds contents to read
    csv_reader = csv.reader(csv_file, delimiter= ',')
    #read header row first and skip
    csv_header = next(csv_file)

    #count each row of data after header to obtain number of months
    monthcount = 0
    #set counter of Profits/Losses as total starting at 0
    total = 0
    #create list to store the change throughout all months
    change_list = []
    #create change counter to save change in variable and store in change_list
    change = 0
    #set a previous profit equal to 0 to start counter
    previous_profit = 0
    #create average_change variable that is obtained when all changes are stored in change_list
    average_change = 0
    #create list to store the months with the changes in profits each month
    month_list = []
    #store the greatest increase in profits in variable
    increase = ['',0]
    #store the greatest decrease in profits in variable
    decrease = ['',9999999]
    #read each row of data after header
    for row in csv_reader:
        #count each row of data after header to obtain the number of months in csv file
        monthcount +=1
        #add the values in the profits column to obtain the total profits/losses
        total += int(row[1])
        #if the value stored in previous_profit is not equal to 0...
        if previous_profit != 0:
            #store the change as the value in profits column minus the value in the previous row
            change = round(float(row[1]),2) - previous_profit
            #store the new change value in the list of changes
            change_list = change_list + [change]
            #store the month in which the change is happening
            month_list = month_list + [row[0]]
            #set previous profit as the current row in profits column
            previous_profit = float(row[1])
        #if the value stored in previous_profit is 0...
        else:
            #set previous profit as the current row in profits column
            previous_profit = float(row[1])
        
        

        #if the current change is greater than the stored greatest increase...
        if change>increase[1]:
            #store current change as new greatest increase value
            increase[1] = round(change)
            #store current month as new greatest increase month
            increase[0] = row[0]
        #if the current change is smalles than the stored greatest decrease...
        if change<decrease[1]:
            #store current change as the new greatest decrease value
            decrease[1] = round(change)
            #store current months as the new greatest decrease value
            decrease[0] = row[0]
    #calculate the average change by adding all change values stored in the list by the length of the list
    average_change = sum(change_list)/len(change_list)

    #print financial analysis summary including the number of months in csv file, the total profits/losses, 
    #the average change and the greatest increase and decrease in profits
    print('Financial Analysis')
    print('-------------------------------')
    print(f'Total Months: {monthcount}')
    print(f'Total: ${total}')
    print(f'Average Change: ${round(average_change,2)}')
    print(f'Greatest Increase in Profits: {increase[0]} (${increase[1]})')
    print(f'Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})')

#create analysis summary file and save in analysis folder
analysis = os.path.join('Analysis','analysis.txt')

#open analysis file in write mode
with open(analysis, 'w') as text_file:
    #write summary on analysis file
    text_file.write(f'''Financial Analysis
-------------------------------
Total Months: {monthcount}
Total: ${total}
Average Change: ${round(average_change,2)}
Greatest Increase in Profits: {increase[0]} (${increase[1]})
Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})''')
    #close analysis file
    text_file.close()

