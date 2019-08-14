
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

freq_data = []

###################################
#
###################################
def read_freq_file():
  global freq_data

  with open('freq.data', 'r') as file:
    del freq_data[:]
    for line in file:
      freq_data.append(int(line))    

###################################
#
###################################
def show_freq():
  global freq_data
 
  max_y = 63
  max_x = 63
  color = (0,0,255)

  image = Image.new("RGB", (total_columns,total_rows))
  draw = ImageDraw.Draw(image)

  for x in range(0,max_x):
    try:
      mapped_freq = freq_data[x]
    except:
      print("freq data issue index "+str(x))
      break;

    if mapped_freq < 0:
       mapped_freq = 0
    if mapped_freq > max_y:
       mapped_freq = max_y
    mapped_freq = max_y - mapped_freq
    draw.line((x, max_y, x, mapped_freq),fill=color) 
  
  matrix.SetImage(image,0,0)

###################################
# Main loop 
###################################
err_count = 0


try:
  print("Press CTRL-C to stop")
  while True:
    try:
      read_freq_file()
    except:
      err_count = err_count + 1
      print("read error: "+str(err_count))
      continue
    show_freq()

  time.sleep(1)

except KeyboardInterrupt:
  exit(0)
