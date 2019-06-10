import csv
from collections import Counter
import json

with open('data.csv') as f:
        # we are using DictReader because we want our information to be in dictionary format.
    rolling_stones_list = list(csv.DictReader(f))

#print(rolling_stones_list[:4])


#Find by name - Takes in a string that represents the name of an album. Should
#return a dictionary with the correct album, or return None.

def find_name(name, search_list):
    for item in search_list:
        if 'album' in item:
            if name == item['album']:
                return item
        elif 'name' in item:
            if name == item['name']:
                return item
    return None

#Find by rank - Takes in a number that represents the rank in the list of top
#albums and returns the album with that rank. If there is no album with that
#rank, it returns None.

def find_rank(rank, search_list):
    for item in search_list:
        if 'rank' in item:
            if str(rank) == item['rank']:
                return item
        elif 'number' in item:
            if str(rank) == item['number']:
                return item
    return None
#print(find_album_rank('501'))

#Find by year - Takes in a number for the year in which an album was released
#and returns a list of albums that were released in that year.
#If there are no albums released in the given year, it returns an empty list.

def find_year(year, search_list):
    in_that_year = []
    for item in search_list:
        if str(year) == item['year']:
            in_that_year.append(item)
    return in_that_year
# print(len(find_album_year('1976')))
# print(find_album_year('2012'))

#Find by years - Takes in a start year and end year. Returns a list of all
# albums that were released on or between the start and end years.
#If no albums are found for those years, then an empty list is returned.

def find_year_range(start,end,search_list):
    in_range_years = []
    for item in search_list:
        if int(item['year']) >= int(start) and int(item['year']) <= int(end):
            in_range_years.append(item)
    return in_range_years
#print(find_album_year_range(1953,1957))

#Find by ranks - Takes in a start rank and end rank. Returns a list of albums
#that are ranked between the start and end ranks. If no albums are found for
#those ranks, then an empty list is returned.

def find_rank_range(start,end,search_list):
    in_range_ranks = []
    for item in search_list:
        if 'rank' in item:
            if int(item['rank']) >= int(start) and int(item['rank']) <= int(end):
                in_range_ranks.append(item)
        elif 'number' in item:
            if int(item['number']) >= int(start) and int(item['number']) <= int(end):
                in_range_ranks.append(item)
    return in_range_ranks
#print(find_album_rank_range(499,700))

#All titles - Returns a list of titles for each album.

def all_titles(search_list):
    titles_list = []
    if 'name' in search_list[0]:
        for item in search_list:
            titles_list.append(item['name'])
    elif 'album' in search_list[0]:
        for item in search_list:
            titles_list.append(item['album'])
    return titles_list

#All artists - Returns a list of artist names for each album.

def all_artists(search_list):
    artist_list = []
    for item in search_list:
        artist_list.append(item['artist'])
    return artist_list

#Artists with the most albums - Returns the artist with the highest amount of
#albums on the list of top albums
# def artist_most_albums():
#   occurence_count = Counter(all_album_artists())
#   print(occurence_count)
#   print()
#   print(occurence_count.most_common(1))
#   print()
#   print(occurence_count.most_common(1)[0])
#   print()
#   print(occurence_count.most_common(1)[0][0])
#   return

def artist_most_popular(search_list):
  occurence_count = Counter(all_artists(search_list))
  return occurence_count.most_common(1)[0][0]


#Most popular word - Returns the word used most in amongst all album titles
# def most_pop_word(search_list):
#     title_string = " ".join(all_titles(search_list)).lower()
#     title_string = title_string.replace('!', '')
#     title_string = title_string.replace('?', '')
#     title_string = title_string.replace('(', '')
#     title_string = title_string.replace(')', '')
#     title_string = title_string.replace('"', '')
#     title_string = title_string.replace(',', '')
#     title_string = title_string.replace(':', '')
#     title_string = title_string.replace('/', '')
#     title_string = title_string.replace('-', '')
#     #print(title_string)
#     wc = Counter(title_string.split())
#     #print(wc)
#     return wc.most_common(1)[0][0]

def most_pop_word(search_list):
    all_words = []
    if 'album' in search_list[0]:
        for item in search_list:
            all_words += item['album'].split()
    elif 'name' in search_list[0]:
        for item in search_list:
            all_words += item['name'].split()
    return Counter([word.lower() for word in all_words]).most_common(1)[0][0]


#Histogram of albums by decade - Returns a histogram with each decade pointing
#to the number of albums released during that decade.
# def hist_albums_per_decade

#Histogram by genre - Returns a histogram with each genre pointing to the
#number of albums that are categorized as being in that genre
# def hist_genre


# open the text file in read
text_file = open('top-500-songs.txt', 'r')
# read each line of the text file
# here is where you can print out the lines to your terminal and get an idea
# for how you might think about re-formatting the data
lines = text_file.readlines()

#print(lines)

#take read text file and sort into list of dictionaries
#1) loop through list for each element (in this case each song).
#2) split each element into individual list (for each element)
#3) make each element a dictionary with keys
#4) add each dictionary to list of dictionaries

def list_of_dict_songs(lines):
    song_dict_list = []
    for line in lines:
        split_song = line.split('\t')
        song_dict = {
        'rank' : split_song[0],
        'name' : split_song[1],
        'artist' : split_song[2],
        'year' : split_song[3].replace('\n', '')}
        song_dict_list.append(song_dict)
    return song_dict_list

#print(list_of_dict_songs(lines))


#print(find_rank(30, rolling_stones_list))
#print(find_rank(31, list_of_dict_songs(lines)))

# print(find_year(1957, rolling_stones_list))
# print(find_year(1990, list_of_dict_songs(lines)))

# print(find_year_range(1953,1957,rolling_stones_list))
# print()
# print(find_year_range(1989,1991,list_of_dict_songs(lines)))

# print(find_rank_range(20,23,rolling_stones_list))
# print()
# print(find_rank_range(100,104,list_of_dict_songs(lines)))

# print(all_titles(rolling_stones_list))
# print()
# print(all_titles(list_of_dict_songs(lines)))

# print(all_artists(rolling_stones_list))
# print()
# print(all_artists(list_of_dict_songs(lines)))

file = open('track_data.json', 'r')
json_data = json.load(file)

print(json_data)

# albumWithMostTopSongs - returns the name of the artist and album that has that
# most songs featured on the top 500 songs list
#
# albumsWithTopSongs - returns a list with the name of only the albums that have
#tracks featured on the list of top 500 songs
#
# songsThatAreOnTopAlbums - returns a list with the name of only the songs
#featured on the list of top albums
#
# top10AlbumsByTopSongs - returns a histogram with the 10 albums that have the
# most songs that appear in the top songs list. The album names should point to
#the number of songs that appear on the top 500 songs list.
#
# topOverallArtist - Artist featured with the most songs and albums on the two
#lists. This means that if Brittany Spears had 3 of her albums featured on the
#top albums listed and 10 of her songs featured on the top songs, she would have
# a total of 13. The artist with the highest aggregate score would be the top
#overall artist.
