import os
import csv

budgetdatacsv = os.path.join("..", 'PyBank', 'budget_data.csv')

# define the function and have it choose what to read from the csv file 
def getStats (budgetData):

    # Total months is the sum of each row in the first column
    totalMonths = int(budgetData[0])

    # Total earnings adding totals in column 2
    totalearnings = int(budgetData[1])

#Calculate average for budgetData in 0 for budget_data.csv. AverageChange in budgetData
AverageChange = sum(int(totalearnings) / totalMonths

    print(f"Total Months: {totalMonths}")
    print(f"Total Earnings: {totalearnings}")
    print(f"Average Change: {AverageChange}")

# open and read the csv file 
        
with open(budgetdatacsv, 'r') as csvfile:
# Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)