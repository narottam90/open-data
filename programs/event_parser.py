import json
import os
import csv

# create the csv file and a writer. Write the first row of headers.

with open('events.csv', 'w', newline ='', encoding = 'utf8') as f:
    writer = csv.writer(f)
    writer.writerow(['Half', 'Time', 'Event', 'Player',
                     'Team', 'XStart', 'YStart', 'XEnd', 'YEnd'])

    # opent the directory where the file is stored
    
    try:
        os.chdir(r'C:\Users\u0168991\Documents\Projects\football\open-data\data\events')
    except:
        print('Unable to change directory.')

    # open the json file

    with open('7298.json', 'r', encoding='utf8') as myFile:
        data = myFile.read()

        # load string data
        obj = json.loads(data)
        count = 0
        for item in obj:
            player = item.get('player', None)
            try:
                print(player['name'])
            except:
                continue
            