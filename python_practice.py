print("Hello world")

# A list of dictionaries

voting_data = []

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})

voting_data.append({"county":"Denver", "registered_voters": 463353})

voting_data.append({"county":"Jefferson", "registered_voters": 432438})

print(voting_data)

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? ")) 

# Total votes in the election
total_votes = int(input("What is the total votes in the election? ")) 

# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100

print("I received " + str(percentage_votes)+"% of the total votes.")

# Decision statements

counties = ["Arapahoe","Denver","Jefferson"] 
if counties[1] == 'Denver':
    print(counties[1])

score = int(input("What is your test score? "))

if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.') 
elif score >= 70:
    print('Your grade is a C.') 
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

# Membership operators


if "El Paso" in counties:
    print("El paso is considered in the counties")
elif "El Paso" not in counties:
    print("El paso is not considered in the counties")

# loop

for element in counties:
    print(element)

# Printing formats

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver",
"registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for dic in voting_data:
    statement = (f"{dic['county']} county has {dic['registered_voters']:,} registered voters")
    print(statement)

