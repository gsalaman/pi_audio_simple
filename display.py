
# Used in main loop
import time

###################################
# Graphics imports, constants and structures
###################################
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw

# this is the size of ONE of our matrixes. 
matrix_rows = 64 
matrix_columns = 64 

# how many matrixes stacked horizontally and vertically 
matrix_horizontal = 1 
matrix_vertical = 1

total_rows = matrix_rows * matrix_vertical
total_columns = matrix_columns * matrix_horizontal

options = RGBMatrixOptions()
options.rows = matrix_rows 
options.cols = matrix_columns 
options.chain_length = matrix_horizontal
options.parallel = matrix_vertical 

#options.hardware_mapping = 'adafruit-hat-pwm' 
#options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
options.hardware_mapping = 'regular'  

options.gpio_slowdown = 2

matrix = RGBMatrix(options = options)

sound_data = []

def read_sound_file():
  global sound_data

  with open('sound.data', 'r') as file:
    del sound_data[:]
    for line in file:
      sound_data.append(int(line))    

###################################
# Main loop 
###################################
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

err_count = 0


try:
  print("Press CTRL-C to stop")
  while True:
    image = Image.new("RGB", (total_columns,total_rows))
    draw = ImageDraw.Draw(image)
    read_sound_file()

    last_x = 0
    last_y = 32

    for data_index in range(0,64):
      new_x = last_x + 1 
      try:
        new_y = sound_data[data_index] 
      except:
        err_count = err_count+1
        print("sound data index issue"+str(err_count))
        continue
      draw.line((last_x, last_y, new_x, new_y),fill=blue) 
      last_x = new_x
      last_y = new_y

    matrix.SetImage(image,0,0)
 
    #print "click!"
    time.sleep(.1)

except KeyboardInterrupt:
  exit(0)
