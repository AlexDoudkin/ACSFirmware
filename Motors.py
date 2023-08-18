from Sensors import hall_Effect, beam_Sensor_Thing
import time
import board
import digitalio 
import busio
from analogio import AnalogIn
import math

 
step = digitalio.DigitalInOut(board.GP16)
step.direction = digitalio.Direction.OUTPUT

mdir= digitalio.DigitalInOut(board.GP17)
mdir.direction = digitalio.Direction.OUTPUT

en = digitalio.DigitalInOut(board.GP18)
en.direction = digitalio.Direction.OUTPUT

fan = digitalio.DigitalInOut(board.GP4)
fan.direction = digitalio.Direction.OUTPUT

a = beam_Sensor_Thing('a',7)
b = beam_Sensor_Thing('b',6)
c = hall_Effect('c',26)


platform_current_Lpos = True
current_pos = 0


class linearMotor:
    en.value = True
    fan.value = True
  
    
    def lowerPlatform(self):
        en.value = False
        fan.value = True
        global platform_current_Lpos
        if platform_current_Lpos == True:
            while a.getInput() == False:
                step.value = True
                time.sleep(0.001)
                step.value = False
                time.sleep(0.001)
            print('csr-pldn-/n/r')
            #platform_current_Lpos = True
        else:
            print('err-5-/n/r')
        fan.value = False
        en.value = True
    
        


    def raisePlatform(self):
        en.value = False
        fan.value = True
        global platform_current_Lpos
        if platform_current_Lpos == True:  
            for i in range(1760):       
                step.value = True
                time.sleep(0.001)
                step.value = False
                time.sleep(0.001)
            print('csr-plup-/n/r')
            #platform_current_Lpos = False
        else:
            print('err-4-/n/r')
        en.value = True
        fan.value = False
        
    
    

  
        

m2step= digitalio.DigitalInOut(board.GP19)
m2step.direction = digitalio.Direction.OUTPUT

m2dir = digitalio.DigitalInOut(board.GP20)
m2dir.direction = digitalio.Direction.OUTPUT

m2en = digitalio.DigitalInOut(board.GP21)
m2en.direction = digitalio.Direction.OUTPUT
    
class rotationMotor:
    m2en.value = True
    m2dir.value = False
    
    
    
    
    def moveOneSampleForward(self):
        m2en.value = False
        global current_pos
        if current_pos == 33:
            while b.getInput() == False:
                m2step.value = True
                time.sleep(0.001)
                m2step.value = False
                time.sleep(0.001)
            current_pos = 0
            print('csr-X0-/n/r')
        else:               
            while c.getInput() == False:
                for i in range(15):
                    m2step.value = True
                    time.sleep(0.001)
                    m2step.value = False
                    time.sleep(0.001)
            #time.sleep(0.5)    
            while c.getInput() == True:
                for i in range(15):
                    m2step.value = True
                    time.sleep(0.001)
                    m2step.value = False
                    time.sleep(0.001)
            for i in range(65):
                m2step.value = True
                time.sleep(0.001)
                m2step.value = False
                time.sleep(0.001)
            current_pos += 1
            print('csr-X' + str(current_pos) + '-/n/r')
        m2en.value = True
        
    def HomeMOSF(self):
            for i in range(15):
                m2step.value = True
                time.sleep(0.001)
                m2step.value = False
                time.sleep(0.001)
    
        
    def MOSF(self):
        m2en.value = False
        global current_pos
        if current_pos == 33:
            while b.getInput() == False:
                m2step.value = True
                time.sleep(0.001)
                m2step.value = False
                time.sleep(0.001)
            current_pos = 0
        else:               
            while c.getInput() == False:
                for i in range(10):
                    m2step.value = True
                    time.sleep(0.001)
                    m2step.value = False
                    time.sleep(0.001)
            #time.sleep(0.5)    
            while c.getInput() == True:
                for i in range(10):
                    m2step.value = True
                    time.sleep(0.001)
                    m2step.value = False
                    time.sleep(0.001)
            for i in range(65):
                m2step.value = True
                time.sleep(0.001)
                m2step.value = False
                time.sleep(0.001)
            current_pos += 1
        m2en.value = True
        
        
        
        
        
        
        
        
    def moveOneSampleBackwards(self):
        m2en.value = False
        m2dir.value = True
        global current_pos
        if current_pos == 0:
            while c.getInput() == True:
                m2step.value = True
                time.sleep(0.001)
                m2step.value = False
                time.sleep(0.001)
            current_pos = 33
            print('csr-X33-/n/r')
        elif current_pos == 1:
            self.home()
            current_pos = 0
            print('csr-X0-/n/r')
        else:               
            while c.getInput() == False:
                for i in range(10):
                    m2step.value = True
                    time.sleep(0.001)
                    m2step.value = False
                    time.sleep(0.001)
            #time.sleep(0.5)    
            while c.getInput() == True:
                for i in range(10):
                    m2step.value = True
                    time.sleep(0.001)
                    m2step.value = False
                    time.sleep(0.001)
                    
            current_pos -= 1
        m2dir.value = False
        m2en.value = True
        
        
        
        
        
    def MOSB(self):
        m2en.value = False
        m2dir.value = True
        global current_pos
        if current_pos == 0:
            while c.getInput() == True:
                m2step.value = True
                time.sleep(0.001)
                m2step.value = False
                time.sleep(0.001)
            current_pos = 33
        elif current_pos == 1:
            self.home()
            current_pos = 0
        else:               
            while c.getInput() == False:
                for i in range(10):
                    m2step.value = True
                    time.sleep(0.001)
                    m2step.value = False
                    time.sleep(0.001)
            #time.sleep(0.5)    
            while c.getInput() == True:
                for i in range(10):
                    m2step.value = True
                    time.sleep(0.001)
                    m2step.value = False
                    time.sleep(0.001)
            current_pos -= 1
        m2dir.value = False
        m2en.value = True
        
        
    def rotate(self,degrees):
        m2en.value = False
        for i in range(math.ceil(((360) / (360 /degrees)) / 0.212)):    
            m2step.value = True
            time.sleep(0.001)
            m2step.value = False
            time.sleep(0.001)
        m2en.value = True
    
    def home(self):
        m2en.value = False
        start = time.time()
        stop_seconds = 50
        
        if(b.pin.value == True):
            self.HomeMOSF()
            print('csr-X0-/n/r')
        else:
            while  b.pin.value == False and time.time() - start < stop_seconds:
                m2step.value = True
                time.sleep(0.001)
                m2step.value = False
                time.sleep(0.001)
                
                if(time.time() - start >= stop_seconds):
                    print('err-3-/n/r')
                    
                if(b.pin.value == True):
                    self.HomeMOSF()
                    print('csr-X0-/n/r')
        m2en.value = True
    
    
    def homing(self):
        m2en.value = False
        global current_pos
        if(b.pin.value == True):
            self.HomeMOSF()
            current_pos = 0
        else:
            while  b.pin.value == False:
                m2step.value = True
                time.sleep(0.001)
                m2step.value = False
                time.sleep(0.001)
                    
                if(b.pin.value == True):
                    self.HomeMOSF()
                    current_pos = 0
        m2en.value = True
        
    
        
        
      

        
                

    def move(self,position):      
        m2en.value = False
        global current_pos
        self.homing()
        for i in range(int(position)):
            self.MOSF()
        print('csr-X' + str(current_pos) + '-/n/r')
        m2en.value = True
        
        
    def getPos(self):
        
        global current_pos
        print('csr-X' + str(current_pos) + '-/n/r')
        m2en.value = True
    
    def setPos(self,position):
        
        global current_pos
        current_pos = position
        print('csr-X' + str(current_pos) + '-/n/r')
        m2en.value = True
        
    def getPlatformState(self):
        global platform_current_Lpos
        if platform_current_Lpos == True:
            print('csr-plup-/n/r')
        else:
            print('csr-pldn-/n/r')
            
    def getVolatage(self):
        for i in range(100):
            print(c.getInput())
            time.sleep(0.3)
   
        
                
            
    
                   
                    

