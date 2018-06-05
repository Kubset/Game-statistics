import reports
FILE = "game_stat.txt"
YEAR = 2000
GENRE = "RPG"
TITLE = "Populous"


print(reports.count_games(FILE))
print(reports.decide(FILE, YEAR))
print(reports.get_latest(FILE))
print(reports.count_by_genre(FILE, GENRE))
print(reports.get_line_number_by_title(FILE, TITLE))
print(reports.sort_abc(FILE))
print(reports.get_genres(FILE))
print(reports.when_was_top_sold_fps(FILE))

print(reports.get_most_played(FILE))
print(reports.sum_sold(FILE))
print(reports.get_selling_avg(FILE))
print(reports.count_longest_title(FILE))
print(reports.get_date_avg(FILE))
print(reports.get_game(FILE, TITLE))
print(reports.count_grouped_by_genre(FILE))
print(reports.get_date_ordered(FILE))
