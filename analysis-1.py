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

print('\n')
print('Game Preview')
for i in range(5):
    pprint(game_data[i])
    print('\n')

#%% rows in dataset
print('Number of Rows in Profile data:', len(profile_data))
print('Number of Rows in Game data:', len(game_data))

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
#theres not any 0, the False are counted as 0, just as True is counted as 1

#%% create function to convert string to int values

def string_to_int(data, fields):
    for i in data:
        for j in fields:
            value = i[j]
            if value != None and value != 0:
                value = value.replace(',', '')
                value = int(value)
                i[j] = value

#columns to convert (for now)
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

#%% more investigating of the data
count = 0
for player in profile_data:
    if player['position'] == 'QB' and player['current_team'] != None:
        pprint(player)
        print('\n')
        count += 1
        
print('\n')
print('total number of active qb in dataset:', count)

#%% hmm

for player in profile_data:
    if 'Tom Brady' in player['name']:
        pprint(player)

#%%
count = 0
for game in game_data:
    if game['player_id'] == 2240 and game['year'] == 2015:
        pprint(game)
        count += 1
        print('\n')
        
print('total number of games in 2017 with tom brady:', count)





############decide what else needs to be cleaned before analyzing data
    
        