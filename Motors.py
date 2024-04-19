from machine import Pin
import time

step = Pin(16, Pin.OUT)
mdir = Pin(17, Pin.OUT)
en = Pin(18, Pin.OUT)

fan = Pin(4, Pin.OUT)

m2step = Pin(19, Pin.OUT)
m2dir = Pin(20, Pin.OUT)
m2en = Pin(21, Pin.OUT)

lift_sensor = Pin(14, Pin.IN)
home_sensor = Pin(13, Pin.IN)
hall_effect = Pin(5, Pin.IN)


class LinearMotor:
    fan.on()

    def __init__(self):
        # engine value is false to prevent mechanical part from moving
        en.value(False)
        self.platform_raised = False
        self.is_aborted = False

    def lowerPlatform(self):
        while not lift_sensor.value() and not self.is_aborted:
            step.on()
            time.sleep(0.001)
            step.off()
            time.sleep(0.001)

        if lift_sensor.value():
            print('dn')
            self.platform_raised = False

    def raisePlatform(self):
        # todo self.platform_raised can be removed when a raised sensor is added
        # this works well until it is aborted in the middle.
        # Abort callers will have to handle re-positioning to the sensor on restart
        wasAborted = False
        if not self.platform_raised:
            for i in range(1760):
                if not self.is_aborted:
                    step.on()
                    time.sleep(0.001)
                    step.off()
                    time.sleep(0.001)
                else:
                    wasAborted = True
        if not wasAborted:
            print('up')
            self.platform_raised = True



class RotationMotor:
    m2en.value(True)
    m2dir.value(False)

    def __init__(self):
        self.homed = False
        self.current_pos = 0
        self.is_aborted = False

    def home(self):
        m2en.value(False)
        lastPingTime = 0
        if not self.homed:
            while not home_sensor.value() and not self.is_aborted:
                self.performStep()

                if time.time() - lastPingTime >= 3:
                    lastPingTime = time.time()
                    print("homing")

            if home_sensor.value():
                self.homed = True
                self.current_pos = 0

        if self.homed:
            print('home')

        m2en.value(True)

    def performStep(self):
        m2step.on()
        time.sleep(0.001)
        m2step.off()
        time.sleep(0.001)

    def rotateMotor(self, sample=0):
        m2en.value(False)
        m2dir.value(sample < self.current_pos)
        atSample = self.current_pos == sample
        needsMoveOffHome = home_sensor.value()
        homedWhileMoving = False
        needsMoveOffSample = hall_effect.value()
        while not atSample and not homedWhileMoving and not self.is_aborted:
            self.performStep()
            if hall_effect.value() and not needsMoveOffSample:
                needsMoveOffSample = True
                if not m2dir.value():
                    self.current_pos += 1
                else:
                    self.current_pos -= 1
                print('Pos ' + str(self.current_pos))
                atSample = self.current_pos == sample
            elif needsMoveOffSample and not hall_effect.value():
                needsMoveOffSample = False

            if home_sensor.value() and not needsMoveOffHome:
                self.homed = True
                self.current_pos = 0
                homedWhileMoving = True
            elif needsMoveOffHome and not home_sensor.value():
                needsMoveOffHome = False

        if m2dir.value():
            # adjust backwards positioning by moving a bit too far and fixing forward
            while hall_effect.value():
                self.performStep()

            m2dir.value(False)
            while not hall_effect.value():
                self.performStep()

        print('R' + str(self.current_pos))
        m2en.value(True)

    def getPos(self):
        print(str(self.current_pos))
