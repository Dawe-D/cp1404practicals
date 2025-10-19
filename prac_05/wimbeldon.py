"""
CP1404 - Prac 5
Task - Wimbledon
Estimate - 40 mins
Actual   - 40 mins
"""

FILENAME = "wimbledon.csv"


def main():
    champion_data = championship_data(FILENAME)
    champion_times_won = count_wins(champion_data)
    display_championship_details(champion_times_won, champion_data)


def championship_data(filename):
    champion_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            year = parts[0]
            country = parts[1]
            name = parts[2]
            champion_data.append([year, country, name])
    return champion_data


def count_wins(champion_data):
    name_to_wins = {}
    for record in champion_data:
        name = record[2]
        name_to_wins[name] = name_to_wins.get(name, 0) + 1
    return name_to_wins


def display_championship_details(champion_times_won, champion_data):
    print("Wimbledon Champions:")

    longest_name = max(len(name) for name in champion_times_won)

    for name, wins in sorted(champion_times_won.items()):
        print(f"{name:{longest_name}} : {wins}")
    print()
    countries = {champion[1] for champion in champion_data}
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

main()
