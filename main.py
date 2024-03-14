import _thread
from Motors import RotationMotor, LinearMotor

rotationMotor = RotationMotor()
linearMotor = LinearMotor()

while True:
    a = input("")
    try:
        if a == 'U':
            linearMotor.is_aborted = False
            _thread.start_new_thread(linearMotor.raisePlatform, ())
        elif a == 'D':
            linearMotor.is_aborted = False
            _thread.start_new_thread(linearMotor.lowerPlatform, ())
        elif a == 'H':
            rotationMotor.is_aborted = False
            _thread.start_new_thread(rotationMotor.home, ())
        elif a == 'N':
            rotationMotor.is_aborted = False
            _thread.start_new_thread(rotationMotor.moveOneSampleForward, ())
        elif a == 'B':
            rotationMotor.is_aborted = False
            _thread.start_new_thread(rotationMotor.moveOneSampleBackwards, ())
        elif a.isdigit():
            rotationMotor.is_aborted = False
            _thread.start_new_thread(rotationMotor.rotateMotor, (int(a), ))
        elif a == 'P':
            rotationMotor.is_aborted = False
            _thread.start_new_thread(rotationMotor.getPos, ())
        elif a == 'abort':
            rotationMotor.is_aborted = True
            linearMotor.is_aborted = True
        elif a == 'ping':
            print('pong')
    except Exception as e:
        print('exception_acsr ' + str(e.args))
