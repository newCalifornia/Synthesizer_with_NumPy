#####################################################################
## The test to generate sound with NumPy math functions 
## and wrapped with some custom functions
## to generate short tracks.
## Oleg Z. 2026
## Requires:
##     NumPy - comes with default Python istallation
##     sounddevice - Python interface to the sound card
#####################################################################
import numpy as np
import sounddevice as sd ## interface to the sound card

BITRATE = 44100 # Audio standard to digital signals

#####################################################################
## ln - length in seconds
## fr - frequency in Hz
def simple_sound(ln, fr):

    ## Create a time vector (X=coordinate)
    x_0 = np.linspace(0, ln * fr * 2*np.pi, int(ln * BITRATE))

    ## Main signal. Vary params and coefficients
    s_0 = np.sin(x_0)**3 + np.sin(2*x_0)**5 + np.sin(0.5*x_0)**7 + np.sin(np.sin(0.0012*x_0)+0.5*x_0)**7
    ## Normalization
    s_0 = s_0/np.max(s_0)
    
    return s_0
#####################################################################

######################### PUT NOTE ARRAY ############################
def put_note_arr(line_n, note_arr, start_arr):

    for idx in range(len(note_arr)):
        
        bar_int = int(start_arr[idx])
        bar_part = start_arr[idx] - bar_int
    
        br_i = bar_int * BITRATE
        br_j = int(bar_part * BITRATE)
        dst = br_i + br_j
        line_n[dst : dst + len(note_arr[idx])] += note_arr[idx]
    
    return line_n
######################### PUT NOTE ARRAY ############################

## Key & frequencies
C = [65.41, 130.81, 261.63, 523.25]
D = [73.42, 146.83, 293.66, 587.33]
E = [82.41, 164.81, 329.63, 659.25]
F = [87.31, 174.61, 349.23, 698.46]
G = [98, 196, 392, 783.99]
A = [110, 220, 440, 880]
B = [123.47, 246.94, 493.88, 987.77]
#####################################################################

snd_1 = simple_sound(0.25, A[2])
snd_2 = simple_sound(0.25, G[2])
snd_3 = simple_sound(0.25, F[2])
snd_4 = simple_sound(0.25, E[2]) 
snd_5 = simple_sound(0.5, G[2])
snd_6 = simple_sound(0.5, C[2])

## Empty short track
track_0 = np.zeros(4 * BITRATE)

## Put array of sounds into a track
track_0 = put_note_arr(track_0, [snd_1, snd_2, snd_3, snd_4, snd_5, snd_6, snd_6, snd_2, snd_3], [0, 0.25, 0.5, 0.75, 1, 1.5, 2, 2.5, 2.75, 3])

## Play the track
sd.play(track_0, BITRATE)
sd.wait()

print("NumPy sound ..")
#####################################################################
