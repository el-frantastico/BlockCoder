import logging
logging.basicConfig(filename='test.log',level=logging.DEBUG)
from time import sleep
import serial
ser = serial.Serial('/dev/ttyUSB0',9600,timeout=1)

MOVE_UP         = "q1"
MOVE_DOWN       = "q2"
MOVE_LEFT       = "q3"
MOVE_RIGHT      = "q4"
MOVE_FORWARD    = "q5"
MOVE_BACK       = "q6"
NEUTRAL         = "q"
FRONT_SENSOR    = "s1"
RIGHT_SENSOR    = "s2"
LEFT_SENSOR     = "s3"
BACK_SENSOR     = "s4"
READ_SENSOR     = "f"
inString = "3333"

#######  functions to start sensors  #######
## start front sensor
def startFront() :
    ser.write(FRONT_SENSOR)
## start left sensor
def startLeft() :
    ser.write(LEFT_SENSOR)
## start right sensor
def startRight() :
    ser.write(RIGHT_SENSOR)
## start back sensor
def startBack() :
    ser.write(BACK_SENSOR)
## read sensors
def readSensors() :
    ser.flush()
    ser.write(READ_SENSOR)
    temp = '0'
    temp2 = '1'	
    t = inString
    t = ser.read()
    t += ser.read()
    t += ser.read()
    t += ser.read()
    return(t)
#######  functions to read sensors  #######
def readLeftSensor(t):
    return (t[2] == '1')
def readFrontSensor(t):
    return (t[0] == '1')
def readRightSensor(t):
    return (t[1] == '1')
def readBackSensor(t):
    return (t[3] == '1')
#######  functions to control motors  #######
## move up
def moveUp() :
    ser.write(MOVE_UP)
## move down
def moveDown() :
    ser.write(MOVE_DOWN)
## move left
def moveLeft() :
    ser.write(MOVE_LEFT)
## move right
def moveRight() :
    ser.write(MOVE_RIGHT)
## move forward
def moveForward() :
    ser.write(MOVE_FORWARD)
## move back
def moveBack() :
    ser.write(MOVE_BACK)
##  neutral code
def neutral() :
    ser.write(NEUTRAL)
def main():	
    ser.write('x');
    tSet = False
    cSet = False
    nSet = False
    mSet = False
    while(not(tSet and cSet and nSet and mSet)) :
        ser.write('t10000')
        if(ser.read()=='t'):
            tSet = True
        ser.write('c5')
        if(ser.read()=='c'):
            cSet = True
        ser.write('n5')
        if(ser.read()=='n'):
            nSet = True
        ser.write('m10')
        if(ser.read()=='m'):
            mSet = True
    isDoneCalib = '';
    while(True) :
            isDoneCalib = ser.read();
            if(isDoneCalib == 'd') :
                break;
    ser.flush();
    startFront();
    while(ser.read()!='1') :
        startFront();
    startRight();
    while(ser.read()!='2') :
        startRight();
    startLeft();
    while(ser.read()!='3') :
        startLeft();
    startBack();
    while(ser.read()!='4') :
        startBack();
    ser.flush();
    turnAround = False;
    didSee = "3333";
    while(True)   :
        didSee = readSensors();
	logging.debug(didSee);
        forward = False;
        frontSeen = readFrontSensor(didSee);
        rightSeen = readRightSensor(didSee);
        leftSeen = readLeftSensor(didSee);
        rearSeen = readBackSensor(didSee);
        if(turnAround) :
            if(frontSeen) :
                turnAround = False;
                moveForward();
            else :
                moveRight();
        else :
            if(frontSeen)  :
                if(rightSeen) :
                    if(leftSeen) :
                        forward = True;
                    else :
                        forward = True;
                elif(leftSeen) :
                    forward = True;
                elif(rightSeen) :
                    moveRight();
            elif(leftSeen) :
                moveLeft();
            elif(rearSeen) :
                turnAround = True;
            if(forward) :
                moveForward();
        sleep(2);

if __name__ == "__main__":
	main()
