import os
import csv


budgetdatacsv = os.path.join('Python-Challenge', 'budget_data.csv')

# open and read the csv file 
#        
with open(budgetdatacsv, 'r') as csvfile:
# Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
# define the function and have it choose what to read from the csv file 
def Stats (budgetData):

    # Total months is the sum of each row in the first column
    total_months_row = int(budgetData[0])
    total_months_row = 0
    # Total earnings adding totals in column 2
    earningsTotalRow = int(budgetData[1])
    earningsTotalRow = 0

for budgetDataRow in budgetdatacsv:

#Determine the number of rows in the months and earnings columns by counting from the first row
    numberOfRowsinMonthsColumn += total_months_row
    numberOfRowsinTotalEarningsColumn += earningsTotalRow

#Determine the average overall earnings by dividing sum by the total amount of rows 
    average = earningsTotalRow / numberOfRowsinTotalEarningsColumn
    greatestincrease = max (earningsTotalRow) - min (earningsTotalRow)

    if (earningsTotalRow < 0):
        earningsTotalRow = totalloss
    elif (earningsTotalRow >= 0): 
        earningsTotalRow = totalprofit

    next
        
    print ("Financial Analysis: ")    
    print (f"Total Months: {numberOfRowsinMonthsColumn}")
    print (f"Total Earnings: {numberOfRowsinTotalEarningsColumn}")
    print (f"Average Change: {average}")

    if (greatestincrease is totalprofit in earningsTotalRow):
        print (f"Greatest Increase in Profits: {budgetDataRow[0], (greatestincrease)}")
    elif (greatestincrease is totalloss in earningsTotalRow):
        print (f"Greatest Decrease in Profits: {budgetDataRow[0], (greatestincrease)}")
     
#Calculate average for budgetData in 0 for budget_data.csv. AverageChange in budgetData
    #AverageChange = sum(int(totalearnings))/totalMonths 