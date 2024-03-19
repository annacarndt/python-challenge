# import
import csv

# file locations


# define variables to keep track of various items **


# loading the CSV
with open('budget_data.csv', 'r') as file:
    reader = csv.reader(file)

    # handle the header row

    # extract out first row and add to different variables
    # initiate prev_month_profit

    # for loop to loop through the rest of the rows:
    for row in reader: 
        print(row)

        # track totals (month + profit/loss)

        # calculate changes / track changes in a list 
        # *HINT: how do you make the current month's profit number available for next month to use

        # check if the change is the greatest increase seen, if yes, 
        # override greatest increase to be the current change

        # check if the change is the greatest decrease seen, if yes, 
        # override greatest decrease to be the current change


# calculate average monthly changes (sum of a list / len of the list)
    
# print outputs using f-strings

# save output into analysis.txt
