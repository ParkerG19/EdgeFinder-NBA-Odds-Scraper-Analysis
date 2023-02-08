

"""
Not all sportsbooks enter their team names the same way - for this I am creating a universal way
to convert them into a way where they can share a foreign key in the database
i.e - database sores the Chicago Bulls in that exact format "Chicago Bulls"....
DraftKings displays the name as "Chi Bulls" - This script aims to convert it to a normal way of
being able to compare the names
"""


def nameConverter(name):


    abbreviationList = ["ATL Hawks", "BOS Celtics", "BKN Nets", "CHA Hornets", "CHI Bulls", "CLE Cavaliers", "DET Pistons",
                        "GS Warriors", "IND Pacers", "LA Lakers", "MIA Heat", "NO Pelicans", "NY Knicks", "OKC Thunder",
                        "ORL Magic", "PHO Suns", "POR Trail Blazers", "SAC Kings", "SA Spurs", "TOR Raptors", "UTA Jazz",
                        "WAS Wizards", "DAL Mavericks", "DEN Nuggets", "HOU Rockets", "LA Clippers", "MEM Grizzlies",
                        "MIL Bucks", "MIN Timberwolves", "PHI 76ers"]

    fullNameList = ["Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", "Chicago Bulls", "Cleveland Cavaliers",
                    "Detroit Pistons", "Golden State Warriors", "Indiana Pacers", "Los Angeles Lakers", "Miami Heat", "New Orleans Pelicans",
                    "New York Knicks", "Oklahoma City Thunder", "Orlando Magic", "Phoenix Suns", "Portland Trail Blazers",
                    "Sacramento Kings", "San Antonio Spurs", "Toronto Raptors", "Utah Jazz", "Washington Wizards", "Dallas Mavericks",
                    "Denver Nuggets", "Houston Rockets", "Los Angeles Clippers", "Memphis Grizzlies", "Milwaukee Bucks",
                    "Minnesota Timberwolves", "Philadelphia 76ers"]

    indexOfName = abbreviationList.index(name)

    fullName = fullNameList[indexOfName]

    return fullName


