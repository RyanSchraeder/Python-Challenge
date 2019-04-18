import os
import csv

budgetdatacsv = os.path.join('Resources', 'budget_data.csv')

total_months_row = 0
total_revenue = 0 
total_monthly_change = 0
max_increase = 0.00
max_decrease = 0.00
max_increase_date = 0 
max_decrease_date = 0 
current_date = 0 

with open(budgetdatacsv, 'r') as csvfile:
# Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    print(header)

    firstdatarow = next(csvreader)
    print(firstdatarow)
    print(firstdatarow[0],firstdatarow[1])
    total_months_row = total_months_row + 1
    #    total_months_row += 1
    print(total_months_row)
    total_revenue = total_revenue + int(firstdatarow[1])
    previous_revenue = int(firstdatarow[1])


    for budgetDataRow in csvreader:
        #print(budgetDataRow)
        total_months_row = total_months_row + 1
        print(total_months_row)
        current_revenue = int(budgetDataRow[1])
        total_revenue = total_revenue + current_revenue
        
        current_date = budgetDataRow[0]

        current_monthly_change = current_revenue - previous_revenue
        print(current_monthly_change)
        total_monthly_change = total_monthly_change + current_monthly_change
        print("Total monthly change:  "  +  str(total_monthly_change))

            #calculate revenue change for each month and capture max, min values. 
        if total_monthly_change > 1: 
                total_monthly_change = current_revenue - previous_revenue
                total_revenue = total_revenue + total_monthly_change
                total_revenue =  total_revenue + 1  
                
        if total_monthly_change >= 0:
                if total_monthly_change > max_increase :
                    max_increase = total_monthly_change
                    max_increase_date = current_date

        elif total_monthly_change < 0:
                if total_monthly_change < max_decrease:
                    max_decrease = total_monthly_change
                    max_decrease_date = current_date

        #print("max" + str(max_increase)) 
        #print("min" + str(max_decrease))  

        previous_revenue = current_revenue
        avg_change = total_monthly_change / total_months_row
        #print("Average Monthly Change: " + str(avg_change))
    
    print(" ")
    print("Financial Analysis")
    print("-"*50)
    print("Total months  : " + str(total_months_row))
    print("Total Revenue : " + str(total_revenue))
    print("Average Revenue Change $" + str(avg_change))
    print("Greatest Increase in Revenue: " + max_increase_date + " ($" +
            str(max_increase) +")" )
    print("Greatest Decrease in Revenue: " + max_decrease_date + " ($" +
            str(max_decrease) +")" )
    print(" ")

# Check total values to ensure nothing is left out
# print(total_revenue)
# print(total_monthly_change)
# print (avg_change)

# Store all values in a text file and output.txt
with open(outputfile, "w") as txt_file:
    calculated_results = (
    print (" ")
    print ("Financial Analysis")
    print("-"*50)
    print("Total months  : " + str(total_months_row))
    print("Total Revenue : " + str(total_revenue))
    print("Average Revenue Change $" + str(avg_change))
    print("Greatest Increase in Revenue: " + max_increase_date + " ($" +
        str(max_increase) +")" )
    print("Greatest Decrease in Revenue: " + max_decrease_date + " ($" +
        str(max_decrease) +")" )
    print(" ")
    )
    txt_file.write(calculated_results)