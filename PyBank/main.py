import os
import csv

budgetdatacsv = os.path.join('Python-Challenge', 'PyBank', 'budget_data.csv')
    
# define the function and have it choose what to read from the csv file 
def Stats (budgetData):

    # Total months is the sum of each row in the first column
    total_months_row = (budgetData[0])
    total_months_row = 0
    # Total earnings adding totals in column 2
    earningsTotalRow = int(budgetData[1])
    earningsTotalRow = 0

    if (earningsTotalRow < 0):
        earningsTotalRow = totalloss
    elif (earningsTotalRow >= 0): 
        earningsTotalRow = totalprofit

#Determine the number of rows in the months and earnings columns by counting from the first row
    numberOfRowsinMonthsColumn += total_months_row
    numberOfRowsinTotalEarningsColumn += earningsTotalRow

#Determine the average overall earnings by dividing sum by the total amount of rows 
    average = earningsTotalRow / numberOfRowsinTotalEarningsColumn
    greatestincrease = max (earningsTotalRow) - min (earningsTotalRow)
# open and read the csv file 
#        
with open(budgetdatacsv, 'r') as csvfile:
# Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for budgetDataRow in budgetdatacsv:
        Stats(budgetDataRow)   

    print ("Financial Analysis: ")    
    print (f"Total Months: {numberOfRowsinMonthsColumn}")
    print (f"Total Earnings: {numberOfRowsinTotalEarningsColumn}")
    print (f"Average Change: {average}")
    if (greatestincrease is totalprofit in earningsTotalRow):
        print (f"Greatest Increase in Profits: {budgetDataRow[0], (greatestincrease)}")
    elif (greatestincrease is totalloss in earningsTotalRow):
        print (f"Greatest Decrease in Profits: {budgetDataRow[0], (greatestincrease)}")

#Print the results in an extracted .csv
    with open(budgetdatacsv, 'w') as budgetdatacsvexported:
        csvwriter = csv.writer (budgetdatacsvexported, delimiter=",")