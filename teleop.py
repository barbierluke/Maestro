import readchar
import sig_handler

class Teleop:

    motor_forward_speeds = [7500,7500,7500,7500,7500,7500]
    motor_reverse_speeds = [4000,4000,4000,4000,4000,4000]
    motor_no_move_speeds = [6000] * 6
    
    def __init__(self):
        self.motorPositions = self.motor_no_move_speeds
        # want to set speed and accel stuff for each motor
    
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
        elif cmd_char == decoder_str[1]:
            print("Elevating")
        elif cmd_char == decoder_str[2]:
            print("Moving forwards")
        elif cmd_char == decoder_str[3]:
            print("Moving backwards")
        elif cmd_char == decoder_str[4]:
            print("Turning right")
        elif cmd_char == decoder_str[5]:
            print("Turning left")
        elif cmd_char == decoder_str[6]:
            print("Killing")
        else:
            print("Malformed Input")
            print("Input must be dive, elevate, or arrow keys")
            print("Enter 'q' to quit")

    # These should just adjust the motorPositions variable
    def go_down(self):
        # motors 1,3,4,6 must be on
        down_motors = [1,3,4,5]
        # First motor is not 1, it's channel zero so decrease every motor number by one
        down_motors = [0,2,3,4]
        for mot in down_motors:
            self.motorPositions[mot] = motor_forward_speeds[mot]
        pass
    def go_up(self):
        pass
    def go_straight(self):    
        pass
    def go_backwards(self):
        
        pass
    def turn_right(self):
        # decrease one motor and increase the other
        # keep in mind T200's are more powerful
        pass
    def turn_left(self):
        pass
                   
    def kill_motors(self):
        all_motors = [0,1,2,3,4,5]
        for mot in all_motors:
            self.motorPositions[mot] = self.motor_no_move_speeds[mot]
    
    def send_cmd(self, cmd_vec):
        # sends the motor statuses to the pololu through the driver
        # just a for loop through the motorPositions array
        pass

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
