import pyaudio
import struct
#import numpy as np

import time

CHUNK = 1024 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
DEV_INDEX = 0
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input_device_index=DEV_INDEX,input=True,output=False,frames_per_buffer=CHUNK)

try:
  print("Hit ctl-c to exit")
  while (True):
    data = stream.read(CHUNK,exception_on_overflow = False)
    data_int = struct.unpack(str(CHUNK) +'h', data)  
    print(data_int)
    time.sleep(1)
    
except KeyboardInterrupt:
  exit(0)

