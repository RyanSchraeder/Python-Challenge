import os
import csv

#Define file path
budgetdatacsv = joinrealpath('budget_data.csv')

#Read in the csvfile
with open(budget_data, newline="") as csvfile:
    #split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    def totals (budgetDataRow):
        # find the months row
        totalMonthsRow = int(budgetDataRow[0])

        # find the earnings row

        earningsTotalRow = int(budgetDataRow[1])

        #create a list to append values through the loop for each column

        RowsinMonthsColumn = []
        TotalEarningsColumn = []
    #create the loop

    for budgetDataRow in csvreader:
        #append totalMonthsRow
            RowsinMonthsColumn.append(totalMonthsRow),
        #append earningsTotalRow, float to get only whole numbers
            TotalEarningsColumn.append(float(earningsTotalRow)),
        #Determine the average overall earnings by dividing sum by the total amount of rows
            average = sum(int(TotalEarningsColumn) / RowsinMonthsColumn

        print ("Financial Analysis: ")

        print ("---------------------")

        print (f"Total Months: {len(RowsinMonthsColumn)}")

        print (f"Total Earnings: {sum(int(TotalEarningsColumn))}")

        print (f"Average Change: {str(average)}")

        print (f"Greatest Increase in Profits: {max(TotalEarningsColumn)}")

        print (f"Greatest Decrease in Profits: {min(TotalEarningsColumn)}")
