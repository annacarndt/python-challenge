# import
total_months = 0

# file locations
with open('/Users/annaarndt/Desktop/Bootcamp/python-challenge/PyBank/budget_data.csv', 'r') as file:
    
    next(file)
    
    # define each line in the file 
    for line in file:
        total_months += 1

print("Total Months:", total_months)

net_profit_losses = 0

# load cvs
with open('/Users/annaarndt/Desktop/Bootcamp/python-challenge/PyBank/budget_data.csv', 'r') as file:

    next(file)
    for line in file:
        data = line.strip().split(',')
        net_profit_losses += int(data[1])

print("Total:", net_profit_losses)

# define variables 
previous_profit_loss = None
total_change = 0
change_count = 0

# open the csv file
with open('/Users/annaarndt/Desktop/Bootcamp/python-challenge/PyBank/budget_data.csv', 'r') as file:

    next(file)
    for line in file:
        data = line.strip().split(',')
        
        # find profit loss value
        profit_loss = int(data[1])
        
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            total_change += change
            change_count += 1
        previous_profit_loss = profit_loss

# print average change
average_change = total_change / change_count

print("Average change:$", average_change)

# define variables 
max_increase_date = None
max_increase_amount = float('-inf')
previous_profit_loss = None

# open csv file
with open('/Users/annaarndt/Desktop/Bootcamp/python-challenge/PyBank/budget_data.csv', 'r') as file:

    next(file)
    for line in file:
       
        data = line.strip().split(',')
        
        # extract date and profit loss value
        date = data[0]
        profit_loss = int(data[1])
        
        # Iis the change the greatest increase, if yes 
        if previous_profit_loss is not None:
            increase = profit_loss - previous_profit_loss
            
            # is the change the greatest increase, if yes
            if increase > max_increase_amount:
                max_increase_amount = increase
                max_increase_date = date
        
        # override greatest incrase to be current change
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
    next(file)
    
    # 
    for line in file:
        # split line
        data = line.strip().split(',')
        
        date = data[0]
        profit_loss = int(data[1])
        
        # find previous profit and loss 
        if previous_profit_loss is not None:
            decrease = profit_loss - previous_profit_loss
            
            # Update the maximum decrease if necessary
            if decrease < max_decrease_amount:
                max_decrease_amount = decrease
                max_decrease_date = date
    
        previous_profit_loss = profit_loss

        # save output into analysis.txt

print("Greatest decrease in profits:")
print("Date:", max_decrease_date)
print(max_decrease_amount)
