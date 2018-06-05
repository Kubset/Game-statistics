import reports

FILE = "game_stat.txt"
YEAR = 2000
GENRE = "RPG"
TITLE = "Populous"

def export_file(file_name):
    with open(file_name, "w") as f:
        f.write(str(reports.count_games(FILE)) + "\n")
        f.write(str(reports.decide(FILE, YEAR)) + "\n")
        f.write(str(reports.get_latest(FILE)) + "\n")
        f.write(str(reports.count_by_genre(FILE, GENRE)) + "\n")
        f.write(str(reports.get_line_number_by_title(FILE, TITLE)) + "\n")
        f.write(str(reports.sort_abc(FILE)) + "\n")
        f.write(str(reports.get_genres(FILE)) + "\n")
        f.write(str(reports.when_was_top_sold_fps(FILE)) + "\n")
        #part2
        f.write("\n")
        f.write(str(reports.get_most_played(FILE)) + "\n")
        f.write(str(reports.sum_sold(FILE)) + "\n")
        f.write(str(reports.get_selling_avg(FILE)) + "\n")
        f.write(str(reports.count_longest_title(FILE)) + "\n")
        f.write(str(reports.get_date_avg(FILE)) + "\n")
        f.write(str(reports.get_game(FILE, TITLE)) + "\n")
        f.write(str(reports.count_grouped_by_genre(FILE)) + "\n")
        f.write(str(reports.get_date_ordered(FILE)) + "\n")


def main():
    export_file("reports.txt")

if __name__ == '__main__':
    main()

