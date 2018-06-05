import math

def count_games(file_name):
    line = " "
    counter = -1
    with open(file_name, "r") as f:
        while len(line): 
            line = f.readline()
            counter += 1
    return counter


def decide(file_name, year):
    line = " "
    game_properties = []
    with open(file_name, "r") as f:
        while len(line): 
            line = f.readline()
            if len(line) > 0:
                game_properties = line.split("\t")
            if int(game_properties[2]) == year:
                return True
        return False


def get_latest(file_name):
    line = " "
    game_properties = []
    lastest_year = 0
    name_of_game = ""
    with open(file_name, "r") as f:
        while len(line): 
            line = f.readline()
            if len(line) > 0:
                game_properties = line.split("\t")
            if int(game_properties[2]) > lastest_year:
                lastest_year = int(game_properties[2])
                name_of_game = game_properties[0]
        
        
        return name_of_game


def count_by_genre(file_name, genre):
    file_text = ""
    lines_list = []
    game_properties = []
    genre_counter = 0
    with open(file_name, "r") as f:
        file_text = f.read()
        lines_list = file_text.split("\n")
        for i in range(0,len(lines_list)-1):
            game_properties = lines_list[i].split("\t")
            if game_properties[3] == genre:
                genre_counter += 1
        return genre_counter
            

def get_line_number_by_title(file_name, title):
    lines_list = []
    game_properties = [] 
    with open(file_name, "r") as f:
        file_text = f.read()
        lines_list = file_text.split("\n")
        for i in range(0,len(lines_list)-1):
            game_properties = lines_list[i].split("\t")
            if game_properties[0] == title:
                return i+1
        raise ValueError


def sort_abc(file_name):
    lines_list = []
    game_titles = [] 
    with open(file_name, "r") as f:
        file_text = f.read()
        lines_list = file_text.split("\n")
        for i in range(0,len(lines_list)-1):
            game_titles.append(lines_list[i].split("\t")[0])
    
    for i in range(len(game_titles)-1, 0, -1):
        for j in range(0,i):
            if game_titles[j].upper() > game_titles[j+1].upper():
                game_titles[j], game_titles[j+1] = game_titles[j+1], game_titles[j]
    return game_titles


def get_genres(file_name):
    lines_list = []
    game_genres = [] 
    with open(file_name, "r") as f:
        file_text = f.read()
        lines_list = file_text.split("\n")
        for i in range(0,len(lines_list)-1):
            game_genres.append(lines_list[i].split("\t")[3])
    
    game_genres = list(set(game_genres))

    for i in range(len(game_genres)-1, 0, -1):
        for j in range(0,i):
            if game_genres[j].upper() > game_genres[j+1].upper():
                game_genres[j], game_genres[j+1] = game_genres[j+1], game_genres[j]
    return game_genres


def when_was_top_sold_fps(file_name):
    lines_list = []
    game_properties = []
    copies_sold = 0
    with open(file_name, "r") as f:
        file_text = f.read()
        lines_list = file_text.split("\n")
    for i in range(0,len(lines_list)-1):
        game_properties = lines_list[i].split("\t")
        if game_properties[3] == "First-person shooter" and float(game_properties[1]) > copies_sold:
            copies_sold = float(game_properties[1])
            year_of_release = game_properties[2]
    if copies_sold:
        return int(year_of_release)
    else:
        raise ValueError


#part 2


def get_most_played(file_name):
    lines_list = []
    game_properties = []
    copies_sold = 0
    game_title = ""
    with open(file_name, "r") as f:
        file_text = f.read()
        lines_list = file_text.split("\n")
    for i in range(0,len(lines_list)-1):
        game_properties = lines_list[i].split("\t")
        if float(game_properties[1]) > copies_sold:
            copies_sold = float(game_properties[1])
            game_title = game_properties[0]
    return game_title


def sum_sold(file_name):
    lines_list = []
    game_properties = []
    total_copies_sold = 0
    with open(file_name, "r") as f:
        file_text = f.read()
        lines_list = file_text.split("\n")
    for i in range(0,len(lines_list)-1):
        game_properties = lines_list[i].split("\t")
        total_copies_sold += float(game_properties[1])
    return total_copies_sold    


def get_selling_avg(file_name):
    with open(file_name, "r") as f:
        lines_number = len(f.readlines())
    
    return sum_sold(file_name)/lines_number

    
def count_longest_title(file_name):
    lines_list = []
    game_properties = []
    max_length_title = 0
    with open(file_name, "r") as f:
        file_text = f.read()
        lines_list = file_text.split("\n")
    for i in range(0,len(lines_list)-1):
        game_properties = lines_list[i].split("\t")
        if len(game_properties[0]) > max_length_title:
            max_length_title = len(game_properties[0])
    return max_length_title    


def get_date_avg(file_name):
    lines_list = []
    game_properties = []
    sum_of_years = 0
    with open(file_name, "r") as f:
        file_text = f.read()
        lines_list = file_text.split("\n")
    for i in range(0,len(lines_list)-1):
        game_properties = lines_list[i].split("\t")
        sum_of_years += int(game_properties[2])
    return math.ceil(sum_of_years/(len(lines_list)-1))


def get_game(file_name, title):
    lines_list = []
    game_properties = []
    sum_of_years = 0
    with open(file_name, "r") as f:
        file_text = f.read()
        lines_list = file_text.split("\n")
    for i in range(0,len(lines_list)-1):
        game_properties = lines_list[i].split("\t")
        game_properties[1] = float(game_properties[1])
        game_properties[2] = int(game_properties[2])
        if game_properties[0] == title:
            return game_properties


def count_grouped_by_genre(file_name):
    lines_list = []
    game_properties = []
    genre_count_dictionary = {}
    with open(file_name, "r") as f:
        file_text = f.read()
        lines_list = file_text.split("\n")
    for i in range(0,len(lines_list)-1):
        game_properties = lines_list[i].split("\t")
        genre_count_dictionary[game_properties[3]] = 0
    for i in range(0,len(lines_list)-1):
        game_properties = lines_list[i].split("\t")
        genre_count_dictionary[game_properties[3]] += 1
    return genre_count_dictionary


def get_date_ordered(file_name):
    lines_list = []
    game_properties = []
    game_title = []
    game_year = []
    alphabetical_sorted = []
    with open(file_name, "r") as f:
        file_text = f.read()
        lines_list = file_text.split("\n")
    for i in range(0,len(lines_list)-1):
        game_properties = lines_list[i].split("\t")
        game_title.append(game_properties[0])
        game_year.append(game_properties[2])
    for i in range(1, len(game_year)+1):
        for j in range(0,len(game_year)-1):
            if game_year[j] > game_year[j+1]:
                game_year[j], game_year[j+1] = game_year[j+1], game_year[j]
                game_title[j], game_title[j+1] = game_title[j+1], game_title[j]   
    i=0
    while i < len(game_year):
        partly_sort = sorted(game_title[i:i+game_year.count(game_year[i])])
        i += game_year.count(game_year[i])
        partly_sort.reverse()
        alphabetical_sorted += partly_sort
    alphabetical_sorted.reverse()
    return alphabetical_sorted
