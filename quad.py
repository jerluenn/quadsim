import numpy as np
import casadi as c 


class Quad:

    def __init__(self, mass, J, mu):

        self.mass = mass 
        self.J = J
        self.x = np.zeros(3)
        self.theta = np.zeros(3)
        self.x_dot = np.zeros(3)
        self.theta_dot = np.zeros(3)
        self.gravity = 9.81 
        self.thrust = np.zeros(4) 
        self.rotate_body_to_world = np.array(
            [[],
            [],
            []])
        self.rotate_world_to_body = np.transpose(self.rotate_body_to_world)
        self.drag_mu = np.diag([mu, mu, 0])

    def updateStates(self):

        mg = np.array(
            [[0],
            [0],
            [self.gravity*self.mass]])
        thrust_body = np.array([
            [0],
            [0],
            [sum(self.thrust)]])
        thrust_world = np.dot(self.rotate_body_to_world, thrust_body)
        drag_force = np.dot(self.drag_mu, self.x_dot)
        self.x_dd = mg + thrust_world + drag_force

        self.theta_dd = 0 

if __name__ == "__main__": 

    crazyflie = Quad(0.1, np.diag([0.1, 0.1, 0.1]), 0.8)
    print(crazyflie)