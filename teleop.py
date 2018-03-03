import readchar
import sig_handler
import maestro

class Teleop:

    motor_forward_speeds = [7500,7500,7500,7500,7500,7500]
    motor_reverse_speeds = [4000,4000,4000,4000,4000,4000]
    motor_no_move_speeds = [6000] * 6
    motors = [0,1,2,3,4,5]
    forward = 1530*4
    backward = 1470*4
    stop = 6000
    turning = False

    def __init__(self):
        self.motorPositions = self.motor_no_move_speeds
        self.control = maestro.Controller()
        # set speed and initial positions for all motors
        for m in self.motors:
            self.control.setAccel(m,4)
            self.control.setSpeed(m,20)
            self.control.setTarget(m,self.stop)
    
    def make_movement(self, cmd_char):
        # some sort of if block to decide
        # d = dive
        # e = elevate
        # A = forward
        # B = Backward
        # C = Turn right
        # D = Turn left
        decoder_str = ['d','e','A','B','C','D',' ']

        # decode movement
        # dive
        if cmd_char == decoder_str[0]:
            print("Diving")
            self.go_down()
        elif cmd_char == decoder_str[1]:
            print("Elevating")
            self.go_up()
        elif cmd_char == decoder_str[2]:
            print("Moving forwards")
            self.go_straight()
        elif cmd_char == decoder_str[3]:
            print("Moving backwards")
            self.go_back()
        elif cmd_char == decoder_str[4]:
            print("Turning right")
            self.turn_right()
        elif cmd_char == decoder_str[5]:
            print("Turning left")
            self.turn_left()
        elif cmd_char == decoder_str[6]:
            print("Killing")
            self.kill_motors()
        else:
            print("Malformed Input")
            print("Input must be dive, elevate, or arrow keys")
            print("Enter 'q' to quit")
        # output the positions to the motors
        self.send_cmd()

    # These should just adjust the motorPositions variable
    def go_down(self):
        # First motor is not 1, it's channel zero so decrease every motor number by one
        down_motors = [0,2,3,5]
        for m in down_motors:
            # we were going up before
            if self.motorPositions[m] == self.backward:
                self.motorPositions[m] = self.stop
            else: # now go down
                self.motorPositions[m] = self.forward
                
    def go_up(self):
        down_motors = [0,2,3,5]
        for m in down_motors:
            # we were going down before
            if self.motorPositions[m] == self.forward:
                self.motorPositions[m] = self.stop
            else: # now go up
                self.motorPositions[m] = self.backward
        
    def go_straight(self):
        straight_motors = [1,4]
        if self.turning == True:
            self.motorPositions[1] = self.stop
            self.motorPositions[4] = self.stop
        
        for m in straight_motors:
            # stop going backward
            if self.motorPositions[m] == self.backward:
                self.motorPositions[m] = self.stop
            else:
                self.motorPositions[m] = self.forward
        self.turning = False
                
    def go_back(self):
        straight_motors = [1,4]        
        if self.turning == True:
            self.motorPositions[1] = self.stop
            self.motorPositions[4] = self.stop

        for m in straight_motors:
            # stop going forward
            if self.motorPositions[m] == self.forward:
                self.motorPositions[m] = self.stop
            else:
                self.motorPositions[m] = self.backward
        self.turning = False
                
    def turn_right(self):
        for_motor = 1
        back_motor = 4
        if self.turning == False:
            self.motorPositions[1] = self.stop
            self.motorPositions[4] = self.stop
        # backward -> stop
        # stop -> forward
        if self.motorPositions[for_motor] == self.backward:
            self.motorPositions[for_motor] = self.stop
        else:
            self.motorPositions[for_motor] = self.forward
        # other motor is forward -> stop
        # other motor stop -> backward
        if self.motorPositions[back_motor] == self.forward:
            self.motorPositions[back_motor] = self.stop
        else:
            self.motorPositions[back_motor] = self.backward
        self.turning = True
                    
    def turn_left(self):
        if self.turning == False:
            self.motorPositions[1] = self.stop
            self.motorPositions[4] = self.stop

        for_motor = 4
        back_motor = 1
        # backward -> stop
        # stop -> forward
        if self.motorPositions[for_motor] == self.backward:
            self.motorPositions[for_motor] = self.stop
        else:
            self.motorPositions[for_motor] = self.forward
        # other motor is forward -> stop
        # other motor stop -> backward
        if self.motorPositions[back_motor] == self.forward:
            self.motorPositions[back_motor] = self.stop
        else:
            self.motorPositions[back_motor] = self.backward
                   
    def kill_motors(self):
        for m in self.motors:
            self.motorPositions[m] = self.stop # stop
    
    def send_cmd(self):
        # sends the motor statuses to the pololu through the driver
        # just a for loop through the motorPositions array
        for m in self.motors:
            self.control.setTarget(m, self.motorPositions[m])

if __name__ == "__main__":
    print("Beginning Teleoperation")
    teleop = Teleop()
    string = None
    while True:
        # Read the input each time
        string = readchar.readkey()
        if len(string) > 1:
            c = string[2]
        else:
            c = string
        if string == 'q':
            break
        teleop.make_movement(c)
        
    print("Exiting")
