# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # defining variables
    rowcount = 0
    netProfitLoss = 0
    average_change = 0

    # Creating a list to store the profit/loss values
    profit_loss = []
    
    # Creating a list to store the month of the profit/loss values
    profit_loss_month = []

    # Creating a list to store the month wise change in profit/loss values
    profit_loss_change = []
    
    for row in csvreader:

        rowcount = rowcount + 1
        netProfitLoss = netProfitLoss + int(row[1])
        
        profit_loss.append(row[1])
        profit_loss_month.append(row[0])
        

    # appending values in profit_loss_change table by comparing current month with previous month values 
    for x in range (1, len(profit_loss)):
        profit_loss_change.append(int(profit_loss[x]) - int(profit_loss[x-1]))

        
    # Calculating the average change by 
    # dividing the sum of month wise change amounts by 
    # the total number of records in the profit_loss_change table   

    average_change = sum(profit_loss_change) / len(profit_loss_change)

    # finding out Greatest Increase in profits values

    greatest_increase_in_profits = max(profit_loss_change)
    
    # finding out the index of the value of the 'greatest_increase_in_profits' from profit_loss_change table

    index_for_greatest_increase_in_profits = profit_loss_change.index(greatest_increase_in_profits)
        
    # finding out the month of the change from profit_loss_change_month table using 'index_for_greatest_increase_in_profits'
    # adding one to varaibale because profit_loss_change table starts from row 2 as it wasa  comparison of the current month vs previous month.

    greatest_increase_in_profits_month = profit_loss_month[index_for_greatest_increase_in_profits + 1]

    
# finding out Greatest decrease in profits values

    greatest_decrease_in_profits = min(profit_loss_change)
    
    # finding out the index of the value of the 'greatest_decrease_in_profits' from profit_loss_change table

    index_for_greatest_decrease_in_profits = profit_loss_change.index(greatest_decrease_in_profits)
        
    # finding out the month of the change from profit_loss_change_month table using 'index_for_greatest_decrease_in_profits'
    # adding one to varaibale because profit_loss_change table starts from row 2 as it was a  comparison of the current month vs previous month.

    greatest_decrease_in_profits_month = profit_loss_month[index_for_greatest_decrease_in_profits + 1]

    # Printing to the Terminal

    print(f"Financial Analysis")
    print(" ")
    print(f"----------------------------")
    print(" ")
    print(f"Total Months: {rowcount}")
    print(" ")
    print(f"Total: ${netProfitLoss}")   
    print(" ")

     # print value till 2 decimal places
    print(f"Average Change : ${average_change:.2f}")
    print(" ")

    print(f"Greatest Increase in Profits : {greatest_increase_in_profits_month} (${greatest_increase_in_profits})")
    print(" ")
    
    print(f"Greatest Decrease in Profits : {greatest_decrease_in_profits_month} (${greatest_decrease_in_profits})")
    
    # Creating a new text file in analysis folder

    Textfilepath = os.path.join("Analysis", "analysis.txt")
    f = open(Textfilepath, "x")

    # Writing intCreating a new text file in analysis folder

    # defining the path
    textfilepath = os.path.join("Analysis", "analysis.txt")

    # creating the text file with write attribute
    textfile = open(Textfilepath, "w")

    # writing to text file
    textfile.write("Financial Analysis \n")
    textfile.write("\n")
    textfile.write("---------------------------- \n")
    textfile.write("\n")
    textfile.write(f"Total Months: {rowcount} \n")
    textfile.write("\n")
    textfile.write(f"Total: ${netProfitLoss} \n")
    textfile.write("\n")
    textfile.write(f"Average Change : ${average_change:.2f} \n")
    textfile.write("\n")
    textfile.write(f"Greatest Increase in Profits : {greatest_increase_in_profits_month} (${greatest_increase_in_profits}) \n")
    textfile.write("\n")
    textfile.write(f"Greatest Decrease in Profits : {greatest_decrease_in_profits_month} (${greatest_decrease_in_profits}) \n")
