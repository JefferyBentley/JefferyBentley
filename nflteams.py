# nflteams.py

'''If the user enters the name of a conference (either ‘AFC’ or ‘NFC’),
prompt them for a division (‘East’, ‘North’, ‘South’, or ‘West’) and print out the names of the corresponding teams.

If the user enters the name of a team, print out the corresponding conference and division
 (e.g., if the user enters ‘Seattle Seahawks’, print ‘NFC West’).

If the user enters input that doesn’t match your data, prompt them again.'''

def get_team():
    conference = input("What is the name of the conference (AFC or NFC)?: ")
    division = input("What is the name of the division (North, South East or West) ")
    newstr = "".join((conference, division))
    conferences = [
                  {'conf':'AFCEast', 'teams': ['Buffalo Bills', 'Miami Dolphins', 'New York Jets', 'New England Patriots']},
                  {'conf':'AFCWest', 'teams': ['Denver Broncos', 'Kansas City Chiefs', 'Oakland Raiders', 'San Diego Chargers']},
                  {'conf':'AFCNorth', 'teams':['Baltimore Ravens', 'Cincinatti Bengals', 'Cleveland Browns', 'Pittsburgh Steelers']},
                  {'conf':'AFCSouth', 'teams':['Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Tennessee Titans']},
                  {'conf':'NFCEast', 'teams': ['Dallas Cowboys', 'New York Giants', 'Philadelphia Eagles', 'Washington Redskins']},
                  {'conf':'NFCWest', 'teams': ['Arizona Cardinals', 'Los Angeles Rams', 'San Francisco 49ers', 'Seattle Seahawks']},
                  {'conf':'NFCNorth','teams':['Chicago Bears', 'Detroit Lions', 'Green Bay Packers', 'Minnesota Vikings']},
                  {'conf':'NFCSouth', 'teams':['Atlanta Falcons', 'Carolina Panthers', 'New Orleans Saints', 'Tampa Bay Buccaneers']}
    ]
    for uinput in conferences:
         if newstr in uinput['conf']:
            return print(uinput['teams'])
            print()
            break
    print("Unknown conference {}".format(conference))
    return 'UNK'



''' Given a team name return its division '''



def get_division():
    team = str(input("Which team would you like to know the Conference and Division for?: "))
    divisions = [
        {'name': 'AFC'' ''East', 'teams': ['Buffalo Bills', 'Miami Dolphins', 'New York Jets', 'New England Patriots']},
        {'name': 'AFC'' ''North', 'teams': ['Baltimore Ravens', 'Cincinatti Bengals', 'Cleveland Browns', 'Pittsburgh Steelers']},
        {'name': 'AFC'' ''South', 'teams': ['Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Tennessee Titans']},
        {'name': 'AFC'' ''West', 'teams': ['Denver Broncos', 'Kansas City Chiefs', 'Oakland Raiders', 'San Diego Chargers']},
        {'name': 'NFC'' ''East', 'teams': ['Dallas Cowboys', 'New York Giants', 'Philadelphia Eagles', 'Washington Redskins']},
        {'name': 'NFC'' ''North', 'teams': ['Chicago Bears', 'Detroit Lions', 'Green Bay Packers', 'Minnesota Vikings']},
        {'name': 'NFC'' ''South', 'teams': ['Atlanta Falcons', 'Carolina Panthers', 'New Orleans Saints', 'Tampa Bay Buccaneers']},
        {'name': 'NFC'' ''West', 'teams': ['Arizona Cardinals', 'Los Angeles Rams', 'San Francisco 49ers', 'Seattle Seahawks']}
    ]
    for division in divisions:
        if team in division['teams']:
            return print(division['name'])
            break
    print ("Unknown division for {}".format(team))
    return 'UNK'


def main():

    print(" NFL Teams Menu: ")
    print("1. Get teams by conference and division: ")
    print("2. Enter team to get conference and divsion: ")
    print("Enter ' 1 ' or ' 2 ' ")
    choice = int(input())
    if choice == 1:
        get_team()
    if choice == 2:
        get_division()
    else:
        exit
        

main()
