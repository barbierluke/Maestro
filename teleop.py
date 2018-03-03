import readchar

class Teleop:

    def __init__(self):
        self.motorPositions = [6000] * 6

        # read in the yaml file for the motor parameters
        # This'll serve as a starting point for future dives
        pass

    def read_input(self):
        # returns the inputted char
        pass
    
    def print_input(self):
        # prints the inputted char
        pass
    
    def decide_movement(self, cmd):
        # some sort of if block to decide
        pass

    # These should just adjust the motorPositions variable
    def go_down(self):
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
        # space bar?
        # set all to 6000
        pass
    
    def send_cmd(self, cmd_vec):
        # sends the motor statuses to the pololu through the driver
        # just a for loop through the motorPositions array
        pass

if __name__ == "__main__":
    c = readchar.readkey()
    print("Your words:")
    print(len(c))
    print(c[2])
