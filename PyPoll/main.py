# import variable
total_votes = 0

# open csv
with open('/Users/annaarndt/Desktop/Bootcamp/python-challenge/PyPoll/Resources/election_data.csv', 'r') as file:
    next(file)
    for line in file:
        total_votes += 1

print("Total Votes:", total_votes)

# define "set"
candidates = set()

# create dictionary
candidate_votes = {}
total_votes = 0

# open cvs
with open('/Users/annaarndt/Desktop/Bootcamp/python-challenge/PyPoll/Resources/election_data.csv', 'r') as file:
    next(file)
    for line in file:
        data = line.strip().split(',')
        
        # take canididate name
        candidate_name = data[2]
        
        # change vote count
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1
        total_votes += 1

# percentage of votes each candidate won
candidate_percentages = {}
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    candidate_percentages[candidate] = percentage

# print candidates and votes
for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    print(f"{candidate}: {votes} votes ({percentage:.2f}% of total votes)")

candidate_votes = {}

# open cvs
with open('/Users/annaarndt/Desktop/Bootcamp/python-challenge/PyPoll/Resources/election_data.csv', 'r') as file:
    next(file)
    for line in file:
        data = line.strip().split(',')
        candidate_name = data[2]

        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

# find candidate with highest votes 
winner = max(candidate_votes, key=candidate_votes.get)

print("Winner:")
print(winner)