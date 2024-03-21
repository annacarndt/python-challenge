# Initialize count of Months 
total_months = 0

# Open the CSV file
with open('/Users/annaarndt/Desktop/Bootcamp/python-challenge/PyBank/budget_data.csv', 'r') as file:
    # Skip the header
    next(file)
    
    # Iterate over each line in the file
    for line in file:
        # Increment the count for each line
        total_months += 1

print("Total Months:", total_months)

# Initialize net total
net_profit_losses = 0

# Open the CSV file
with open('/Users/annaarndt/Desktop/Bootcamp/python-challenge/PyBank/budget_data.csv', 'r') as file:
    # Skip the header
    next(file)
    
    # Iterate over each line in the file
    for line in file:
        # Split the line by comma
        data = line.strip().split(',')
        # Extract profit/loss value and add it to the net total
        net_profit_losses += int(data[1])

print("Total:", net_profit_losses)

# Initialize variables
previous_profit_loss = None
total_change = 0
change_count = 0

# Open the CSV file
with open('/Users/annaarndt/Desktop/Bootcamp/python-challenge/PyBank/budget_data.csv', 'r') as file:
    # Skip the header
    next(file)
    
    # Iterate over each line in the file
    for line in file:
        # Split the line by comma
        data = line.strip().split(',')
        
        # Extract the profit/loss value
        profit_loss = int(data[1])
        
        # If previous profit/loss exists, calculate the change
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            total_change += change
            change_count += 1
        
        # Update the previous profit/loss value
        previous_profit_loss = profit_loss

# Calculate the average change
average_change = total_change / change_count

print("Average change:$", average_change)

# Initialize variables
max_increase_date = None
max_increase_amount = float('-inf')
previous_profit_loss = None

# Open the CSV file
with open('/Users/annaarndt/Desktop/Bootcamp/python-challenge/PyBank/budget_data.csv', 'r') as file:
    # Skip the header
    next(file)
    
    # Iterate over each line in the file
    for line in file:
        # Split the line by comma
        data = line.strip().split(',')
        
        # Extract the date and profit/loss value
        date = data[0]
        profit_loss = int(data[1])
        
        # If previous profit/loss exists, calculate the increase
        if previous_profit_loss is not None:
            increase = profit_loss - previous_profit_loss
            
            # Update the maximum increase if necessary
            if increase > max_increase_amount:
                max_increase_amount = increase
                max_increase_date = date
        
        # Update the previous profit/loss value
        previous_profit_loss = profit_loss

print("Greatest increase in profits:")
print("Date:", max_increase_date)
print(max_increase_amount)

# Initialize variables
max_decrease_date = None
max_decrease_amount = float('inf')
previous_profit_loss = None

# Open the CSV file
with open('/Users/annaarndt/Desktop/Bootcamp/python-challenge/PyBank/budget_data.csv', 'r') as file:
    # Skip the header
    next(file)
    
    # Iterate over each line in the file
    for line in file:
        # Split the line by comma
        data = line.strip().split(',')
        
        # Extract the date and profit/loss value
        date = data[0]
        profit_loss = int(data[1])
        
        # If previous profit/loss exists, calculate the decrease
        if previous_profit_loss is not None:
            decrease = profit_loss - previous_profit_loss
            
            # Update the maximum decrease if necessary
            if decrease < max_decrease_amount:
                max_decrease_amount = decrease
                max_decrease_date = date
        
        # Update the previous profit/loss value
        previous_profit_loss = profit_loss

print("Greatest decrease in profits:")
print("Date:", max_decrease_date)
print(max_decrease_amount)
