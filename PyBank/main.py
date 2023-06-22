
import os # Import the os module
import csv # Module for reading CSV file

budget_data_csv_file_path = r"C:\Users\drabi\OneDrive\Desktop\Bootcamp\Assignments\Week3Challenge\PyBank\Resources\budget_data.csv"
analysis_results_text_file_path = r"C:\Users\drabi\OneDrive\Desktop\Bootcamp\Assignments\Week3Challenge\PyBank\Analysis\Financial_Analysis_Results.txt"

# Initialize variables
total_months = 0
total_profit_and_loss_amount = 0
previous_profit_and_loss_amount = 0
change_sum = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""

with open(budget_data_csv_file_path,  encoding = 'UTF-8') as csv_file:  # Open the CSV using the UTF-8 encoding
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)  # Skip the header row
    
      
    for row in csv_reader: # Read each row of data after the header 
        month = row[0]  # Get the month value from the row
        profit_and_loss_amount = int(row[1])    # Get the profit/loss amount from the row and convert it to an integer
        
        total_months += 1   # Count the number of months
        total_profit_and_loss_amount += profit_and_loss_amount  # Accumulate the total profit/loss over the period.
        
        if previous_profit_and_loss_amount != 0: # Check if there is a valid previous profit/loss amount available.
            change = profit_and_loss_amount - previous_profit_and_loss_amount   # Calculate the change in profit/loss
            change_sum += change    # Accumulate the total change in profit/loss over the period.
                        
            if change > greatest_increase:  # Check if the current change is the greatest increase in profit/loss
                greatest_increase = change  # Update the value of greatest_increase with the current change if it is larger
                greatest_increase_month = month # Update the month corresponding to the greatest increase in profit/loss
            
            if change < greatest_decrease:  # Check if the current change is the greatest decrease in profit/loss
                greatest_decrease = change  # Update the value of greatest_decrease with the current change if it is smaller
                greatest_decrease_month = month # Update the month corresponding to the greatest decrease in profit/loss
        
        previous_profit_and_loss_amount = profit_and_loss_amount    # Set the current profit/loss amount as the previous profit/loss amount for the next iteration
    
    average_change = change_sum / (total_months - 1) # Calculates the average change in profit/loss per month

# Print the financial analysis results to the console
analysis_results = [
"\nFinancial Analysis",
"----------------------------",
f"Total Months: {total_months}",
f"Total: ${total_profit_and_loss_amount:,}",
f"Average Change: ${average_change:,.2f}",
f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})",
f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})"
]

# Write the console output to a text file
with open(analysis_results_text_file_path, 'w') as output_file:
    for result in analysis_results:
        print(result)  # Print the result to the console
        output_file.write(result + "\n")  # Write the result to the text file

print("\nPlease see Financial_Analysis_Results.txt file to see the results.\n")
