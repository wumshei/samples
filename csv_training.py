from os import scandir,remove

from project_constants import OUTPATH, TRAINING_DIR, TRAINING_CSV_FILENAME
from project_constants import getPath

#FILE FOR CREATING A CSV WITH LABELS
csv_loc = getPath(TRAINING_DIR,TRAINING_CSV_FILENAME)
#FIRST CREATE A FRESH CSV
try:
    remove(csv_loc)
except:
    print("no csv to delete")

#OPEN CSV IN APPEND MODE
f = open(csv_loc, 'a+')
#WRITE COLUMN TITLES
f.write("path,label\n")

#SCAN OUR OUTPUT FOLDER FOR DIRECTORIES.
dirs = [d for d in scandir(OUTPATH) if d.is_dir()]
#FOR EACH DIRECTORY IN OUR OUTPUT FOLDER
for dir in dirs:
    #IF THERE ARE SUBFOLDERS PRESENT, ADD THEM TO OUR LIST OF DIRECTORIES TO SCAN
    more = [d for d in scandir(dir) if d.is_dir()]
    for sub in more:
        dirs.append(sub)
    #FOR EACH FILE IN OUR LIST OF DIRECTORIES TO SCAN,
    for file in scandir(dir):
        if file.is_file():
            #WRITE ENTRY FOR FILEPATH, AND DIRECTORY NAME (WHICH SHOULD CORRESPOND TO THE RELEVANT LABEL)
            row = f"{file.path},{dir.name}\n"
            f.write(row)
f.close()

