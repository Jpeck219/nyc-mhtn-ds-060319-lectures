import csv
from collections import Counter

with open('data.csv') as f:
        # we are using DictReader because we want our information to be in dictionary format.
    rolling_stones_list = list(csv.DictReader(f))

#print(rolling_stones_list[:4])


#Find by name - Takes in a string that represents the name of an album. Should
#return a dictionary with the correct album, or return None.

def find_album_name(album_name):
    for stone in rolling_stones_list:
        if album_name == stone['album']:
            return stone
    return None
#print(find_album_name('Revolver'))

#Find by rank - Takes in a number that represents the rank in the list of top
#albums and returns the album with that rank. If there is no album with that
#rank, it returns None.

def find_album_rank(album_rank):
    for stone in rolling_stones_list:
        if str(album_rank) == stone['number']:
            return stone
    return None
#print(find_album_rank('501'))

#Find by year - Takes in a number for the year in which an album was released
#and returns a list of albums that were released in that year.
#If there are no albums released in the given year, it returns an empty list.

def find_album_year(year):
    albums_in_that_year = []
    for stone in rolling_stones_list:
        if str(year) == stone['year']:
            albums_in_that_year.append(stone)
    return albums_in_that_year
# print(len(find_album_year('1976')))
# print(find_album_year('2012'))

#Find by years - Takes in a start year and end year. Returns a list of all
# albums that were released on or between the start and end years.
#If no albums are found for those years, then an empty list is returned.

def find_album_year_range(start,end):
    albums_in_range = []
    for stone in rolling_stones_list:
        if int(stone['year']) >= int(start) and int(stone['year']) <= int(end):
            albums_in_range.append(stone)
    return albums_in_range
#print(find_album_year_range(1953,1957))

#Find by ranks - Takes in a start rank and end rank. Returns a list of albums
#that are ranked between the start and end ranks. If no albums are found for
#those ranks, then an empty list is returned.

def find_album_rank_range(start,end):
    albums_in_range = []
    for stone in rolling_stones_list:
        if int(stone['number']) >= int(start) and int(stone['number']) <= int(end):
            albums_in_range.append(stone)
    return albums_in_range
#print(find_album_rank_range(499,700))

#All titles - Returns a list of titles for each album.

def all_album_titles(): #can you input a promt that would put inputted range into function
    album_titles_list = []
    for stone in rolling_stones_list:
        album_titles_list.append(stone['album'])
    return album_titles_list
#print(all_album_titles())

#All artists - Returns a list of artist names for each album.

def all_album_artists():
    album_artist_list = []
    for stone in rolling_stones_list:
        album_artist_list.append(stone['artist'])
    return album_artist_list
#print(all_album_artists())



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

def artist_most_albums():
  occurence_count = Counter(all_album_artists())
  return occurence_count.most_common(1)[0][0]


#Most popular word - Returns the word used most in amongst all album titles
def most_pop_word_albums():
    #alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
    title_string = " ".join(all_album_titles()).lower()
    title_string = title_string.replace('!', '')
    title_string = title_string.replace('?', '')
    title_string = title_string.replace('(', '')
    title_string = title_string.replace(')', '')
    title_string = title_string.replace('"', '')
    title_string = title_string.replace(',', '')
    title_string = title_string.replace(':', '')
    title_string = title_string.replace('/', '')
    title_string = title_string.replace('-', '')
    #print(title_string)
    wc = Counter(title_string.split())
    #print(wc)
    return wc.most_common(1)[0][0]
#print(most_pop_word_albums())


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
