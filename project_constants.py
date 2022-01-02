#Constants
#paths
import os
import pathlib


TARGETDIR = "./splice/sounds/packs"
OUTPATH = "./outputs"
TRAINING_DIR = "./training"
TRAINING_CSV_FILENAME = "labelled_data.csv"

#functions
def getPath(p1, p2):
    #returns the path of a filename when passed the path from relative folder ("./") to its parent folder.
    temp = p1+'/'+p2
    return pathlib.Path(temp)

def getFilesFromDir(dir):
    output = []
    for roots,dirs,files in os.walk(dir):
        for file in files:
            output.append(f"{roots}/{file}")
    return output