def Temperature():
    temperature = int(input("What is the temperature outside? "))
    if temperature > 80:
        print("Turn on the AC.")
    else:
        print("Open the windows.")
#Temperature()

def grades():
    #What is the score?
    score = int(input("What is your test score? "))

    # Determine the grade.
    if score >= 90:
        print('Your grade is an A.')
    else:
        if score >= 80:
            print('Your grade is a B.')
        else:
            if score >= 70:
                print('Your grade is a C.')
            else:
                if score >= 60:
                    print('Your grade is a D.')
                else:
                    print('Your grade is an F.')
#grades()    

def grades_improved():
    # What is the score?
    score = int(input("What is your test score? "))

    # Determine the grade.
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
#grades_improved()

def voting():
    my_votes = int(input('How many votes did you receive? '))
    total_votes = int(input("What was the total amount of votes received? "))
    Percentage = (my_votes/total_votes)*100
    print("You had " + str(Percentage)+" %"+" of the votes")
#voting()

def counties():
    counties = ["Arapahoe","Denver","Jefferson"]
    if "El Paso" in counties:
        print("El Paso is in the list of counties.")
    else:
        print("El Paso is not the list of counties.")
#counties()

def counties2():
    counties = ["Arapahoe","Denver","Jefferson"]
    if "Arapahoe" in counties and "El Paso" in counties:
        print("Arapahoe and El Paso are in the list of counties.")
    else:
        print("Arapahoe or El Paso is not in the list of counties.")
#counties2()

def counties3():
    counties = ["Arapahoe","Denver","Jefferson"]
    if "Arapahoe" in counties or "El Paso" in counties:
        print("Arapahoe or El Paso is in the list of counties.")
    else:
        print("Arapahoe and El Paso are not in the list of counties.")
#counties3()

def counties4():
    counties = ["Arapahoe","Denver","Jefferson"]
    if "Arapahoe" in counties and "El Paso" not in counties:
        print("Only Arapahoe is in the list of counties.")
    else:
        print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")
#counties4()

def while_loops():
    x = 0
    while x <= 5:
        print(x)
        x = x + 1
#while_loops()

def for_loops():
    counties = ["Arapahoe","Denver","Jefferson"]
    for county in counties:
        print(county)
#for_loops()

def range_function():
    for num in range(5):
        print(num)
#range_function()

def range_index():
    counties = ["Arapahoe","Denver","Jefferson"]
    for i in range(len(counties)):
        print(counties[i])
#range_index()

def dictionary_iteration():
    counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
    for county in counties_dict:
        print(county)
#dictionary_iteration()    

def dictionary_iteration2():
    counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
    for county in counties_dict.keys():
        print(county)
#dictionary_iteration2()

def dictionary_values():
    counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
    for voters in counties_dict.values():
        print(voters)
#dictionary_values()

def dictionary_values2():
    counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
    i = int(input("Method1 or Method2? "))
    if i == 1:
        for county in counties_dict:
            print(counties_dict[county])
    elif i == 2:
        for county in counties_dict:
            print(counties_dict[county])
    else: 
        print("Enter 1 or 2")
#dictionary_values2()

def key_value_pairs():
    counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
    for county, voters in counties_dict.items():
        print(str(county) + " county has " + str(voters) + " registered voters.")
#key_value_pairs()

def list_of_dict():
    voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
    counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
    i = int(input("Method1 or Method2? "))
    if i == 1:
        for county_dict in voting_data:
            print(county_dict)
    elif i == 2:
        for j in range(len(voting_data)):
            print(voting_data[j])
    else:
        print("Choose 1 or 2")
#list_of_dict()

def list_of_dict_values():
    voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
    counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
    for county_dict in voting_data:
        for value in county_dict.values():
            print(value)
#list_of_dict_values()

def list_of_dict_values2():
        voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
        counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
        i = int(input("Method1 or Method2? ")) 
        if i == 1:
            for county_dict in voting_data:
                print(county_dict['registered_voters'])
        elif i ==2:
            for county_dict in voting_data:
                print(county_dict['county'])
        else:
            print("Choose 1 or 2")
#list_of_dict_values2()

def Votes():
    my_votes = int(input("How many votes did you get in the election? "))
    total_votes = int(input("What is the total votes in the election? "))
    print(f"You received {my_votes / total_votes * 100}% of the total votes.")
#Votes()

def Votes2():
    counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
    for county, voters in counties_dict.items():
        print(f"{county} county has {voters} registered voters.")
#Votes2()

def Votes3():
    candidate_votes = int(input("How many votes did the candidate get in the election? "))
    total_votes = int(input("What is the total number of votes in the election? "))
    message_to_candidate = (
        f"You received {candidate_votes:,} number of votes. "
        f"The total number of votes in the election was {total_votes:,}. "
        f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
    print(message_to_candidate)
#Votes3()

def skilldrill1():
    counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
    for x,y in counties_dict.items():
        print(f"{x} county has {y:,} registered voters")
#skilldrill1()

def skilldrill2():
    voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
    for dictionary in voting_data:
        print(f'{dictionary["county"]} county has {dictionary["registered_voters"]:,} registered voters.')
#skilldrill2()


