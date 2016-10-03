#Data
# Serial ----> ()



import numpy as np
import serial

edisonData = serial.Serial('com4', 115200)

class GameState:
    def __init__(self):
        # Global-ish.
        # pole degree of crashed = 20
        self.crashed = False

        # Physics stuff.
        # removing all setup for enviroment
        #self.space = pymunk.Space()
        #self.space.gravity = pymunk.Vec2d(0., 0.)

        # Create init value or desired pos for pole
        self.pole_pos()

        # Record steps.
        # increment epsilon?
        self.num_steps = 0


        # Create some obstacles, semi-randomly.
        # We'll create three and they'll move around to prevent over-fitting.
        # removed cat and obstacles



    def pole_pos(self, theta, omega, r):
      #get value from serial for initialization
      #SERIAL AND POS
        self.pole_body.position = theta, omega
        self.pole_body.angle = r #unable to find another degree
        driving_direction = Vec2d(1, 0).rotated(self.pole_body.angle)
        self.pole_body.apply_impulse(driving_direction)
        self.space.add(self.pole_bodomega, self.pole_shape)

    def motor_speed(self,dof, k):
    #dof needed for to identify which
    # k-value based on action and act as constant to motorspeed
    #
    new_rotate = deg_diff *

    if dof == omega :
        mo

    def motor_step(self, action):
       # 6 actions need to check
       # set speed motor
        if action == -3:  # Turn left.
            #SEND SPEED TO MOTOR
            motor_speed(omega)
            motorspeed_omega = deg_diff_omega *
            motorspeed_theta = deg_diff_theta *
            self.motor.speed -= .2
        elif action == -2:  # Turn right.
            #SEND SPEED TO MOTOR
            self.motor.speed += .2
        elif action == -1:  # Turn right.
            #SEND SPEED TO MOTOR
            self.motor.speed += .2

        elif action == 0:  # Turn right.
            #SEND SPEED TO MOTOR
            self.motor.speed += .2

        elif action == 1:  # Turn right.
            #SEND SPEED TO MOTOR
            self.motor.speed += .2


        elif action == 2:  # Turn right.
            #SEND SPEED TO MOTOR
            self.motor.speed += .2

      # which motor to run
        theta
        driving_direction = Vec2d(1, 0).rotated(self.pole_body.angle)
        self.pole_body.velocity = 100 * driving_direction

        # Update the screen and stuff.

        # Get the current location and the readings there.
        theta, omega = self.pole_body.position
        readings = self.get_sonar_readings(theta, omega, self.pole_body.angle)
        state = np.array([readings])

        # Set the reward.
        # pole crashed when any reading == 1
        if self.pole_is_crashed(readings):
            self.crashed = True
            reward = -500
            self.recover_from_crash(driving_direction)
        else:
            # Higher readings are better, so return the sum.
            reward = -5 + int(self.sum_readings(readings) / 10)
        self.num_steps += 1

        return reward, state

    def pole_is_crashed(self, readings):
        if readings[0] == 1 or readings[1] == 1 or readings[2] == 1:
            return True
        else:
            return False

    def recover_from_crash(self, driving_direction):
        """
        We hit something, so recover.
        """
        while self.crashed:
            # Go backwards.
            self.pole_body.velocity = -100 * driving_direction
            self.crashed = False
            for i in range(10):
                self.pole_body.angle += .2  # Turn a little.
                screen.fill(THECOLORS["red"])  # Red is spoley!
                draw(screen, self.space)
                self.space.step(1./10)
                if draw_screen:
                    pygame.display.flip()
                clock.tick()

    def sum_readings(self, readings):
        """Sum the number of non-zero readings."""
        tot = 0
        for i in readings:
            tot += i
        return tot


if __name__ == "__main__":
    game_state = GameState()
    while True:
        game_state.motor_step((random.randint(0, 2)))
