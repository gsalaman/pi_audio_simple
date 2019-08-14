# pi_audio_simple

Looks like pyaudio collides with the matrix code for pulse generation.
Since we're running a real OS, I think I can have one program (process?) 
generating the sound data, and another using the matrix to display it!

sample_generator.py is the generator program.  It creates a file called "sound.data" with the scaled data points...it does the bias and scaling.

display.py reads that file and displays it onto the RGB matrix.  There can be collisions that cause indexing errors...to deal with those I'm simply using a "try" block and having the exception just continue (skipping that update).

## FFT notes
Trying numpy first...the pip install didn't work.  Instead, use:
sudo apt-get install python-numpy
