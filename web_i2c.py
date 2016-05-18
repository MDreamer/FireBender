import webiopi
import os
import sys
from webiopi.devices.analog.pca9685 import PCA9685

pca0 = PCA9685(0x40,500)

# setup function is automatically called at WebIOPi startup
def setup():
    return

# loop function is repeatedly called by WebIOPi 
def loop():
    
    max = pca0.pwmMaximum()      # returns PCA9685 maximum integer value
    pca0.pwmWrite(0, max)        # set 100% on PCA9685 pwm channel 0 (integer value)
    print max
    print pca0
    webiopi.sleep(3)

    pca0.pwmWrite(0, (max/2) )       # set 0% on PCA9685 pwm channel 0 (integer value)        

    webiopi.sleep(3)

    pca0.pwmWrite(0, 0)        # set 0% on PCA9685 pwm channel 0 (integer value)        

    webiopi.sleep(3)
    # gives CPU some time before looping again
    #webiopi.sleep(5)

# destroy function is called at WebIOPi shutdown
def destroy():
    return