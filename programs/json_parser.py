import json
import os
import csv

directory_in_str = r'C:\Users\u0168991\Documents\Projects\football\open-data\data\matches\11'
directory = os.fsencode(directory_in_str)

with open('output.csv', 'w', newline='', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(["Match Date", "Kick Off Time", "Home Team", "HGoals", "Away Team", "AGoals", "Season"])

# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
# This error occurs because you are using a normal string as a path. You can use one of the following solutions to fix your problem.
# put r before your normal string it converts normal string to raw string

    try:
        os.chdir(r'C:\Users\u0168991\Documents\Projects\football\open-data\data\matches\11')
    except:
        print('Unable to change directory')

    # loop through the all the json files in the directory of folder 11

    try:
        for file in os.listdir(directory_in_str):
            filename = os.fsdecode(file)
            # print(filename)

        # open the json file
            with open(filename, 'r', encoding = 'utf8') as myFile:
                data = myFile.read()

            # load string data to obj
                obj = json.loads(data)
                for item in obj:
                    md = item['match_date']
                    ko = item['kick_off']
                    homeTeam = item['home_team']['home_team_name']
                    homeScore = item['home_score']
                    awayTeam = item['away_team']['away_team_name']
                    awayScore = item['away_score']
                    season = item['season']['season_name']
                    # print(md, ko, homeTeam, homeScore, awayTeam, awayScore, season)

                    rowData = [md, ko, homeTeam, homeScore, awayTeam, awayScore, season]
                    writer.writerow(rowData)
    except:
        quit()
