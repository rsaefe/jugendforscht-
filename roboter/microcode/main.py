#Micro-Python, use this on M5Flow platform and create a Remote+ UI with the elements in the code, if you don't give the exact name to the Control, then it will be a problem, probably it won't run.
from m5stack import *
from m5ui import *
from uiflow import *
import hat
remoteInit()

setScreenColor(0x111111)

hat_roverc_0 = hat.get(hat.ROVERC)

joystick_x_value = None
joystick_y_value = None
motor = None



Title = M5Title(title="Roboter v1.2", x=25, fgcolor=0xFFFFFF, bgcolor=0x1f3b65)

from numbers import Number




def button_MotLock_callback():
  global motor, joystick_x_value, joystick_y_value 
  if motor == 0:
    motor = (motor if isinstance(motor, Number) else 0) + 1
  else:
    motor = (motor if isinstance(motor, Number) else 0) + 0

def image_VideoCAM_callback():
  global motor, joystick_x_value, joystick_y_value 
  pass
def joystick_Joystick_callback(joystick_x_value, joystick_y_value):
  global motor 
  if motor == 0:
    hat_roverc_0.SetSpeed(joystick_x_value, joystick_y_value, 0)
  else:
    pass

def button_2_callback():
  global motor, joystick_x_value, joystick_y_value 
  if motor == 0:
    hat_roverc_0.SetSpeed(0, 0, 100)
  else:
    pass

#Grab your own ID!!!
lcd.qrcode('https://flow.m5stack.com/remote?id=undefined', 45, 104, 70)
motor = (motor if isinstance(motor, Number) else 0) + 0
