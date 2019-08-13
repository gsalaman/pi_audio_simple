import pyaudio
import struct
#import numpy as np

CHUNK = 1024 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
DEV_INDEX = 0
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input_device_index=DEV_INDEX,input=True,output=True,frames_per_buffer=CHUNK)

data = stream.read(CHUNK)

data_int = struct.unpack(str(CHUNK) +'h', data)  #unpack as 16-bit signed int.
print(data_int)

