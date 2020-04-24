import os

# code to loop through files in a directory

directory_in_str = r'C:\Users\u0168991\Documents\Projects\football\open-data\data\matches\11'

directory = os.fsencode(directory_in_str)

for file in os.listdir(directory_in_str):
    filename = os.fsdecode(file)
    print(filename)