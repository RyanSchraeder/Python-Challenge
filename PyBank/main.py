import os
import csv

#Define file path
budgetdatacsv = os.path.join('Python-Challenge', 'PyBank', 'budget_data.csv')

# define the function and have it choose what to read from the csv file
def totals (budgetDataRow):

    # Total months is the sum of each row in the first column

    totalMonthsRow = int(budgetDataRow[0])

    # Total earnings adding totals in column 2

    earningsTotalRow = int(budgetDataRow[1])

    #Determine the number of rows in the months and earnings columns by counting from the first row

    numberOfRowsinMonthsColumn = []
    numberOfRowsinTotalEarningsColumn = []

    #Determine the average overall earnings by dividing sum by the total amount of rows
    average = 0
    average = sum(int(earningsTotalRow) / numberOfRowsinTotalEarningsColumn

    print ("Financial Analysis: ")
    print ("----")
    print (f"Total Months: {len(numberOfRowsinMonthsColumn)}")
    print (f"Total Earnings: {sum(numberOfRowsinTotalEarningsColumn)}")
    print (f"Average Change: {str(average)}")
    print (f"Greatest Increase in Profits: {max(numberOfRowsinTotalEarningsColumn)}")
    print (f"Greatest Decrease in Profits: {min(numberOfRowsinTotalEarningsColumn)}")

with open(budgetdatacsv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

        for budgetDataRow in budgetdatacsv:
            numberOfRowsinMonthsColumn.append(budgetDataRow[0]),
            numberOfRowsinTotalEarningsColumn.append(float(budgetDataRow[1]))
        print totals (budgetDataRow)

#Calculate average for budgetData in 0 for budget_data.csv. AverageChange in budgetData
    #AverageChange = sum(int(totalearnings))/totalMonths
