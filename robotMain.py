from motorTest2 import Motor
import key as kp
from servoMotor2 import Servo
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.IN)
GPIO.setup(29,GPIO.IN)



kp.init()

motor=Motor(3,5,7,11,13,15)
servo=Servo(16,31)
angle=90
angle2=90

while True:
    if(GPIO.input(22)):
        motor.stop(2)
        print('metal detected')
        break
    if(GPIO.input(29)==0):
        motor.stop(2)
        print('flame detected')
        break
        
   
    
    if kp.getKey('UP'):
        print('up')
    
        motor.move(0.6,0,1)
    
   
    
    elif kp.getKey('DOWN'):
       
       motor.move(-0.6,0,1)
    elif kp.getKey('b'):
       motor.stop(2)
    
    elif kp.getKey('RIGHT'):
    
       motor.move(0.6,0.4,1)
      
    elif kp.getKey('LEFT'):
       
       motor.move(0.6,-0.4,2)
    elif kp.getKey('a'):
        
        angle=angle-1
        if(angle<0):
            angle=0
            
        servo.motorR(angle)
    elif kp.getKey('d'):
        
        angle=angle+1
        if(angle>180):
            angle=180
        servo.motorR(angle)
    elif kp.getKey('s'):
        angle2=angle2+1
        if(angle2>180):
            angle2=180
        servo.motorL(angle2)
    elif kp.getKey('w'):
        angle2=angle2-1
        if(angle2<0):
            angle2=0
            
        servo.motorL(angle2)
        
    
    else:
        motor.stop(2)
        servo.motorS()