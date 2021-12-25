# read all the samples in /testsamples and subfolders
# atm going to sort on name but will want to read audio data somehow
import os
import re
import shutil
import pathlib

# establish types dictionary
SAMPLE_TYPES = {}
# establish types
HAT_TYPES = ["ohh", "chh", "hat"]
CYMBAL_TYPES = ["crash", "ride", "splash"]
KICK_TYPES = ["kick"]
SNARE_TYPES = ["snr", "snare"]
CLAP_TYPES = ["clap", "clp"]
PERC_TYPES = ["perc", "percussion", "shaker", "shake"]
# Constants
# paths
TARGETDIR = "./testsamples"
OUTPATH = "outputs"


# add to dict
SAMPLE_TYPES["hat"] = HAT_TYPES
SAMPLE_TYPES["cymbal"] = CYMBAL_TYPES
SAMPLE_TYPES["kick"] = KICK_TYPES
SAMPLE_TYPES["snare"] = SNARE_TYPES
SAMPLE_TYPES["perc"] = PERC_TYPES
SAMPLE_TYPES["clap"] = CLAP_TYPES

# Functions


def getPath(p1, p2):
    temp = p1+'/'+p2
    return pathlib.Path(temp)

# CLEAN TESTSAMPLES OF ASD FILES FIRST


def main():
    # clear outputs folder
    shutil.rmtree(f"./outputs")
    # make empty outputs folder
    os.mkdir(f"./{OUTPATH}")

    for roots, dirs, files in os.walk(TARGETDIR):
        for filename in files:
            tempPath = getPath(roots, filename)
            if re.match(r".*\.asd", filename):
                os.remove(tempPath)
            else:
                for key in SAMPLE_TYPES:
                    try:
                        os.mkdir(f"./outputs/{key}", mode=511, dir_fd=None)
                    except:
                        pass
                    for keyword in SAMPLE_TYPES[key]:
                        if re.search(keyword, filename, re.IGNORECASE):
                            shutil.copyfile(
                                tempPath, f"{OUTPATH}/{key}/{filename}")


main()
