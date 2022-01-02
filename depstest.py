import os
#External deps
import pandas as pd
import numpy as np
import librosa #if anything breaks, its because i literally pasted the _soundfile_data libwhatever.dylib from its thing after renaming
import matplotlib.pyplot as plt
from scipy.io import wavfile
from python_speech_features import mfcc,logfbank
import tensorflow as tf

tf