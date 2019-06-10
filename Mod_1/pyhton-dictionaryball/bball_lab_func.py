#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 09:43:26 2019

@author: jonathanpeck
"""
from dictionaryball import *

#def num_points_scored(name):
    #   if name == game_dictionary['home']['players'][i]:
      #    return game_dictionary['home']['players'][name]['points']
    #   else name == game_dictionary['away']['player'][[i]:
        #   return game_dictionary['away']['player'][name]['points']

def shoe_size(player_name):
    if player_name in game_dictionary['home']['players'].keys():
        return game_dictionary['home']['players'][player_name]['shoe']
    else:
        return game_dictionary['away']['players'][player_name]['shoe']
# print(shoe_size('Ben Gordon'))
# print(shoe_size('Reggie Evans'))
# print(shoe_size('Alan Anderson'))


#home_player_list=[]
#game_dictionary['home']['players'].keys().append(home_player_list)
#clear
#print(home_player_list)
    #home/away
    #players
    #find spec player(argument)
    #return (argument[points])

def num_points_scored(name):
    if name in game_dictionary['home']['players'].keys():
        return game_dictionary['home']['players'][name]['points']
    elif name in game_dictionary['away']['players'].keys():
        return game_dictionary['away']['players'][name]['points']
    return num_points_scored

#print(num_points_scored('Ben Gordon'))

#input=teamname
#output= list of numbers


# def player_numbers(Team_Name):
#     Home_Numbers = []
#     Away_Numbers = []
#     if Team_Name == game_dictionary['home']['team_name']:
#         for team in game_dictionary.values():
#             for player in team['players'].keys():
#                 Home_Numbers.append(team['players'][player]['number'])
#                 print(Home_Numbers)
#
#     elif Team_Name == game_dictionary['away']['team_name']:
#         for team in game_dictionary.values():
#             for player in team['players'].keys():
#                 Away_Numbers.append(team['players'][player]['number'])
#                 print(Away_Numbers)

# print(player_numbers('Brooklyn Nets'))

def player_numbers(Team_Name):
    Home_Numbers = []
    Away_Numbers = []
    if Team_Name == game_dictionary['home']['team_name']:
        for player_name in game_dictionary['home']['players'].keys():
            Home_Numbers.append(game_dictionary['home']['players'][player_name]['number'])
                # print(Home_Numbers)
        return Home_Numbers
    else:
        for player_name in game_dictionary['away']['players'].keys():
            Away_Numbers.append(game_dictionary['away']['players'][player_name]['number'])
                # print(Away_Numbers)
        return Away_Numbers
# print(player_numbers('Brooklyn Nets'))
# print(player_numbers('Charlotte Hornets'))


# def player_numbers(Team_Name):
#     number_list = []
#     for home_or_away in game_dictionary.values():
#         for player in home_or_away['players'].keys():
#             number_list.append(home_or_away['players'][player]['number'])
#     return number_list[0:5]
        # for home_or_away in game_dictionary.values():
        #     for player in home_or_away['players'].keys():
        #         Away_Numbers.append(home_or_away['players'][player]['number'])
        #         print(Away_Numbers)


def player_stats(player_name):
    if player_name in game_dictionary['home']['players'].keys():
        return game_dictionary['home']['players'][player_name]
    elif player_name in game_dictionary['away']['players'].keys():
        return game_dictionary['away']['players'][player_name]
    return player_stats
#
# print(player_stats('Ben Gordon'))
# print(player_stats('Reggie Evans'))

#def big_shoe_rebounds(game_dictionary):
# max of (game_dictionary['home'/'away']['players'][player_name]['shoe'])
def shoe_size_list(game_dictionary):
    for team in game_dictionary.values():
        for player in team['players'].keys():
            return game_dictionary[team]['players'][player]['shoes']

# print(shoe_size_list)

# def find_the_team(team_name):
#     try:
#         return [team for team in game_dict().values() if team['team_name'].lower()== team_name.lower()[0]]
#     except:
#         return 'Team did not play'
