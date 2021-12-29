#read all the samples in /testsamples and subfolders
#atm going to sort on name but will want to read audio data somehow



import os
import re
import shutil
import pathlib
from typing import List
import time

#pip mutagen
from mutagen.wave import WAVE

#establish types dictionary
SAMPLE_TYPES = {}
#establish types
CLOSED_HAT_TYPES = ["chh","closed"]
OPEN_HAT_TYPES = ["ohh", "open"]
HAT_TYPES = [CLOSED_HAT_TYPES,OPEN_HAT_TYPES,"hat","hihat"]
CYMBAL_TYPES = ["cymbal","ride","splash"]
KICK_TYPES = ["kick"]
SNARE_TYPES = ["snr", "snare"]
CLAP_TYPES = ["clap", "clp"]
PERC_TYPES = ["perc", "percussion", "shaker", "shake"]
#Constants
#paths
TARGETDIR = "./splice/sounds/packs"
OUTPATH = "outputs"


#add to dict
SAMPLE_TYPES["hat"] = HAT_TYPES
SAMPLE_TYPES["cymbal"] = CYMBAL_TYPES
SAMPLE_TYPES["kick"] = KICK_TYPES
SAMPLE_TYPES["snare"] = SNARE_TYPES
SAMPLE_TYPES["perc"] = PERC_TYPES
SAMPLE_TYPES["clap"] = CLAP_TYPES

#Functions
def getPath(p1, p2):
    #returns the path of a filename when passed the path from relative folder ("./") to its parent folder.
    temp = p1+'/'+p2
    return pathlib.Path(temp)

def checkLength(roots,filename) -> int:
    #Checks the length of a .wav file. some samples may contain the word "perc" but be music loops, not drums
    try:
        audio = WAVE(getPath(roots,filename))
        try:
            sample_length = int(audio.info.length)
            return sample_length
        except:
            print(f"error 2: {filename}")
            return -1
    except:
        print(f"error: {filename}")
        return -1

def validateLength(type, length) -> bool:
    #up to here
    if type in CYMBAL_TYPES:
        if length < 8:
            return True

def sampleRegexer(lookFor,searchTarget) -> bool:
    escaped = re.escape(lookFor)
    if re.search(rf"([^a-zA-Z])?(?(1)(?!<=[a-zA-Z]{escaped}){escaped}+[^a-zA-Z]+|^{escaped})",searchTarget,re.IGNORECASE) != None:
        return True
    else:
        return False

#set true to re-run sample sorts.
if(True == True):
    #CLEAN TESTSAMPLES OF ASD FILES FIRST

    #clear outputs folder
    shutil.rmtree(f"./outputs")
    #make empty outputs folder
    os.mkdir(f"./{OUTPATH}")

    START_TIME = time.time()
    count = 0
    matchcount = 0
    for roots, dirs, files in os.walk(TARGETDIR):
        for filename in files:
            tempPath = getPath(roots,filename)
            if re.match(r".*\.asd",filename):
                os.remove(tempPath)
            elif re.search("loop",filename,re.IGNORECASE):
                continue
            else:
                count+=1
                for key in SAMPLE_TYPES:
                    try:
                        os.mkdir(f"./outputs/{key}", mode=511, dir_fd=None)
                    except:
                        pass
                    for keyword in SAMPLE_TYPES[key]:
                        if isinstance(keyword,list):
                            for subkey in keyword:
                                try:
                                    os.mkdir(f"./outputs/{key}/{keyword}", mode=511, dir_fd=None)
                                except:
                                    pass
                                if sampleRegexer(subkey,filename):
                                    #dont validate, these words will not be pluralised (hopefully)
                                    matchcount +=1
                                    shutil.copyfile(tempPath, f"{OUTPATH}/{key}/{keyword}/{filename}")
                        else:
                            if sampleRegexer(keyword,filename):
                                if sampleRegexer(f"{keyword}s",filename):
                                    if validateLength(keyword,checkLength(roots,filename)):
                                        matchcount +=1
                                        shutil.copyfile(tempPath, f"{OUTPATH}/{key}/{filename}")
                                    else:
                                        print(f"{filename} might not be the droid you are looking for")
    END_TIME = time.time()
    ELAPSED_TIME = END_TIME - START_TIME
    print(f"complete in {ELAPSED_TIME} seconds, matched {matchcount} of {count} files.")



