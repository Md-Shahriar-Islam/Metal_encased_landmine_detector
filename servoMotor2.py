import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
import key as kp

kp.init()
class Servo():
    def __init__(self,servoPin,servoPin2):
        self.servoPin=servoPin
        self.servoPin2=servoPin2
        GPIO.setup(self.servoPin,GPIO.OUT)
        GPIO.setup(self.servoPin2,GPIO.OUT)
        self.pwma=GPIO.PWM(self.servoPin,50)
        self.pwmb=GPIO.PWM(self.servoPin2,50)
        self.pwma.start(0)
        self.pwmb.start(0)
    def motorR(self,angle):
        DC=1./18.*(angle)+2
        self.pwma.ChangeDutyCycle(DC)
    def motorL(self,angle):
        DC=1./18.*(angle)+2
        self.pwmb.ChangeDutyCycle(DC)
    def motorS(self):
        self.pwma.ChangeDutyCycle(0)
        self.pwmb.ChangeDutyCycle(0)
        
if __name__=='__main__':
    servo=Servo(16,31)
    angle=90
    angle2=90
    while(1):
        if kp.getKey('a'):
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
            servo.motorS()
            
        
    
