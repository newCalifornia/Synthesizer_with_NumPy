####################################################################
## The simplest test to generate sound with NumPy math functions.
## Requires:
##     NumPy - comes with default Python istallation
##     sounddevice - Python interface to the sound card
####################################################################
import numpy as np
import sounddevice as sd ## interface to the sound card

## Create a time vector (X=coordinate)
BITRATE = 44100 # Audio standard to digital signals
LN = 2 # Seconds
FR = 300 # Hz
x_0 = np.linspace(0, LN * FR * 2*np.pi, int(LN * BITRATE))

## Main signal. Vary params and coefficients
s_0 = np.sin(x_0)**3 + np.sin(2*x_0)**5 + np.sin(0.5*x_0)**7 + np.sin(np.sin(0.0012*x_0)+0.5*x_0)**7
## Normalization
s_0 = s_0/np.max(s_0)

## Play the array
sd.play(s_0, BITRATE)
sd.wait()

print("NumPy sound ..")
####################################################################