from Motors import rotationMotor, linearMotor
from Sensors import hall_Effect, beam_Sensor_Thing

import board
import digitalio
import time

while True:  
    a = input()
    try:
        start = a[:3]
        command = a[4:8]
        param = a[9:a.index('-/')]
        indent = a[a.index('-/')+1:]
        
        if start == 'csc':
            if command == 'degr':
                rotationMotor().rotate(int(param))
                print('csr-dg90-/n/r')
            elif command == 'brup':
                linearMotor().raisePlatform()  
            elif command== 'down':
                linearMotor().lowerPlatform()
            elif command == 'home':
                rotationMotor().home()
            elif command == 'next':
                rotationMotor().moveOneSampleForward()
            elif command == 'prev':
                rotationMotor().moveOneSampleBackwards()   
            elif command == 'move':
                rotationMotor().move(param)                 
            elif command == 'pos?':
                rotationMotor().getPos()
            elif command == 'setp':
                rotationMotor().setPos(int(param))
            elif command == 'plp?':
                rotationMotor().getPlatformState()
            elif command == 'onnn':
                led.value = True
                print('on')
            elif command == 'offf':
                led.value = False
                print('off')
            elif command == 'ping':
                print('csr-pong-/n/r')
            elif command == 'stst':
                #print('ok')
                #rotationMotor().getVolatage()
                for i in range(50):
                    print(sensor.value)
                    time.sleep(0.3)
                
            else:
                print('err-6-/n/r')       
        else:
            print('err-1-/n/r')
    except:
        print('err-7-/n/r')
    