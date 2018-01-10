#%% imports
import json
from pprint import pprint

#%% load data to python dicts
profile_data = json.load(open('profile-data.json'))
game_data = json.load(open('games-data.json'))

#%% quick look at data
print('\n')
print('Profile Preview')
for i in range(5):
    pprint(profile_data[i])

print('\n')
print('Game Preview')
pprint(game_data[1000000])

#%% #Create dictionary to count up all 0 in all fields of game stats

zero_dict = {}

for stat in game_data[0]:
    zero_dict[stat] = 0
    
for game in game_data:
    for stat in game:
        count = zero_dict[stat]
        if game[stat] == 0:
            count += 1
            zero_dict[stat] = count

pprint(zero_dict)

#%% convert string data to numerical data 

### not converting dates or height for profile yet
profile_convert_columns = ['current_salary', 
                   'draft_position', 
                   'draft_round', 
                   'draft_year', 
                   'weight']

### NOT converting below list ever/yet
game_not_convert_columns = ['age',
                            'date',
                            'game_location',
                            'game_won',
                            'opponent',
                            'team']

#convert profile strings to int
for player in profile_data:
    for column in profile_convert_columns:
        value = player[column]
        if value != None:
            value = value.replace(',' , '')
            value = int(value)
            player[column] = value
'''
#convert games strings to int
for game in game_data:
    for stat in game:
        if stat not in game_not_convert_columns:
            value = game[stat]
            value = value.replace(',' , '')
            value = int(value)
            game[stat] = value

        '''
    
