import pyaudio
import struct
import numpy as np

import time

CHUNK = 1024 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
DEV_INDEX = 0
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input_device_index=DEV_INDEX,input=True,output=False,frames_per_buffer=CHUNK)
 
#sample_jump = CHUNK/64
sample_jump = 2
sample_scale = 100
sample_bias = 32 

freq_scale = 10

try:
  print("Hit ctl-c to exit")
  while (True):
    data = stream.read(CHUNK,exception_on_overflow = False)
    data_int = struct.unpack(str(CHUNK) +'h', data)  
     
    with open('sound.data','w') as file:
      for point in range(0,CHUNK,sample_jump):
        file.write(str(sample_bias + (data_int[point]/sample_scale))+"\n")
    
    print("time write done")

    Y_k = np.fft.fft(data_int)[0:int(CHUNK/2)]/CHUNK  #fft from numpy
    Y_k[1:] = 2*Y_k[1:] #only grab single sided spectrum
    Pxx = np.abs(Y_k)   #magnitude only
    int_freq = Pxx.astype(int) # truncate them to integers

    with open('freq.data','w') as file:
      for index in range(0,63): 
        file.write(str(int_freq[index]/freq_scale)+"\n")


    print("freq write done")
    time.sleep(1)
    
except KeyboardInterrupt:
  exit(0)

