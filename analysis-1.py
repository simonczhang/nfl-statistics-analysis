#%% imports
import json
from pprint import pprint

#%% load data to python dicts
profile_original = json.load(open('profile-data.json'))
game_original = json.load(open('games-data.json'))

#%% keep original and analysis data separate
profile_data = profile_original
game_data = game_original

#%% quick look at data
print('\n')
print('Profile Preview')
for i in range(5):
    pprint(profile_data[i])

print('\n')
print('Game Preview')
for i in range(5):
    pprint(game_data[i])
#%% #Create dictionary to count up all 0 in all fields of game stats

zero_dict = {}

for stat in game_data[0]:
    zero_dict[stat] = 0
    
pprint(zero_dict)


for game in game_data:
    for stat in game:
        count = zero_dict[stat]
        if game[stat] == 0:
            count += 1
            zero_dict[stat] = count

pprint(zero_dict)

#%% why is there so many 0 for game_won field?

a = set()

for game in game_data:
    value = game['game_won']
    a.add(value)
    
print(a)

#%% create function to convert string to int values

def string_to_int(data, fields):
    for i in data:
        for j in fields:
            value = i[j]
            if value != None and value != 0:
                value = value.replace(',', '')
                value = int(value)
                i[j] = value

profile_convert_columns = ['current_salary', 
                   'draft_position', 
                   'draft_round', 
                   'draft_year', 
                   'weight']

game_convert_columns = ['game_number',
                        'opponent_score',
                        'year',
                        'player_team_score']

#convert profiles and game data
string_to_int(profile_data, profile_convert_columns)
string_to_int(game_data, game_convert_columns)

