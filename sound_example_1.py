####################################################################
## The test to generate sound with NumPy math functions 
## and wrapped with custom functions
## Oleg Z. 20026
## Requires:
##     NumPy - comes with default Python istallation
##     sounddevice - Python interface to the sound card
####################################################################
import numpy as np
import sounddevice as sd ## interface to the sound card

BITRATE = 44100 # Audio standard to digital signals

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
####################################################################

snd_1 = simple_sound(1, 400)
snd_2 = simple_sound(1, 300)
snd_3 = simple_sound(2, 500)

## Empty short track
track_0 = np.zeros(4 * BITRATE)
track_0[0:BITRATE] = snd_1
track_0[BITRATE:2*BITRATE] = snd_2
track_0[2*BITRATE:] = snd_3

## Play the track
sd.play(track_0, BITRATE)
sd.wait()

print("NumPy sound ..")
####################################################################