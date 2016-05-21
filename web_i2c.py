import webiopi
from webiopi.devices.analog.pca9685 import PCA9685
val = 0
val_prev = 0
#pca0
#pca0 = PCA9685(0x40,500)
pca0 = webiopi.deviceInstance("pwm0")
# setup function is automatically called at WebIOPi startup
def setup():
    pca0 = webiopi.deviceInstance("pwm0") # retrieve the device named "mcp" in the configuration
    #return

# loop function is repeatedly called by WebIOPi 
def loop():
    global val, val_prev
    if (val != val_prev):
    #max = pca0.pwmMaximum()      # returns PCA9685 maximum integer value
        pca0.pwmWrite(0, val)        # set 100% on PCA9685 pwm channel 0 (integer value)
        #webiopi.sleep(3)
        val_prev = val
    #print max
    #print pca0
    #webiopi.sleep(3)

    #pca0.pwmWrite(0, (max/2) )       # set 0% on PCA9685 pwm channel 0 (integer value)        

    #webiopi.sleep(3)

    #pca0.pwmWrite(0, 0)        # set 0% on PCA9685 pwm channel 0 (integer value)        
    #webiopi.sleep(3)
    #gives CPU some time before looping again
    #webiopi.sleep(5)
    #destroy function is called at WebIOPi shutdown

def destroy():
    pca0 = webiopi.deviceInstance("pwm0") # retrieve the device named "mcp" in the configuration
    return

# a simple macro to return heater mode
@webiopi.macro
def start_py_Spark():
    global val, val_prev
    if (val == 0):
        val = pca0.pwmMaximum()
    else:
        val = 0
    print "Spark!" + str(val)
    #pca0.pwmWrite(0, max)
    #webiopi.sleep(_time_spark);
    #webiopi.sleep(5)
    #pca0.pwmWrite(0, 0)
    return "Spark!"

