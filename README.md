Auto Calibration Machine Firmware
Written using MicroPython for the Raspberry Pi Pico

| COMMAND                  | PING RESPONSE    | RESPONSE       | DESCRIPTION                                                                                                                                                                                                                                                                                             |
|--------------------------|------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| U                        |                  | up             | Raises the ACS platform to scanning position. It is important to note currently this function does not use a sensor and relies on an approximate location                                                                                                                                               |
| D                        |                  | dn             | Lowers the ACS platform to moving position. This function uses a sensor to determine the correct location                                                                                                                                                                                               |
| H                        | homing           | home           | Rotates the ACS platform until the home position is found, based on a sensor. While homing the ACS returns a ping every 3 seconds to let the caller know the ACS is still connected and completing the command. Home should only need to be done once per startup and the ACS will remember where it is |
| any digit (1, 2, 3, etc) | Pos(current_pos) | R(current_pos) | Rotates the ACS to the requested position. This uses the current position parameter which would be set from either a home(0) or recent move request. It returns a ping everytime the current position is changed, which is based on a sensor reading magnets attached to the bottom of each sample cup  |
| P                        |                  | current_pos    | Returns the current sample position of the ACS.                                                                                                                                                                                                                                                         |
| abort                    |                  |                | Immediately stop any motor movement for the ACS and stops any currently running function from returning pings or final return values                                                                                                                                                                    |
| ping                     |                  | pong           | Returns a value to let the caller know the ACS is still connected                                                                                                                                                                                                                                       |

