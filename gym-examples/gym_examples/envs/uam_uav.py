import numpy as np 
import matplotlib.pyplot as plt

import gymnasium as gym
from gymnasium import spaces


from assets import airspace, airtrafficcontroller, collision_controller
from assets.uav import UAV
import geopandas as gpd
from shapely import Point
import time
from typing import List


#! Warning
'''
Remember this environment will only be used for training,
Therefore there will only be one auto_uav which is built into the uam_env 
'''
#! End 


class Uam_Uav_Env(gym.Env):
    metadata = {"render_mode":["human", "rgb_array"], "render_fps":4}

    def __init__(self, location_name, num_vertiports, num_reg_uav,render_mode=None):
        #airspace,airtrafficcontroller,uav,autonomous_uav,vertiport,
        #from Airspace class
        uam_airspace = airspace.Airspace(location_name)
        #from ATC class
        uam_atc = airtrafficcontroller.ATC(airspace=uam_airspace)
        #from Collision_controller class
        uam_collsion_ctrl = collision_controller.Collision_controller()
        # uav controller 
        #self.controller = controller
        # Initialize sim's vertiports and uavs using ATC
        uam_atc.create_n_random_vertiports(num_vertiports)
        uam_atc.create_n_reg_uavs(num_reg_uav)
        # unpacking atc.vertiports in airspace
        vertiports_point_array = [vertiport.location for vertiport in uam_atc.vertiports_in_airspace]
        # sim data
        self.sim_vertiports_point_array = vertiports_point_array
        self.uav_list:List[UAV] = uam_atc.reg_uav_list 

        print("working")
        pass 

    def _get_obs(self,):
        ### Observation Space
        """
        The observation is a `ndarray` with shape `(4,)` with the values corresponding to the following positions and velocities:
        Maybe N-dimensional? (N : # of uavs)
        | Num | Observation                      | Min                 | Max               |
        |-----|----------------------------------|---------------------|-------------------|
        | 0   | UAVs' states(pos)                | -4.8                | 4.8               |
        | 1   | UAVs' states(speed)              | -Inf                | Inf               |
        | 2   | UAVs' states(ref heading)        | ~ -0.418 rad (-24°) | ~ 0.418 rad (24°) |
        | 3   | UAVs' states(heading_correction) | -Inf                | Inf               |
        """

        pass 

    def _get_info(self,):
        pass 

    def reset(self,):
        pass 

    def step(self,action):
        pass

    def render(self,):
        
        pass

    def _render_frame(self,):
        pass

    def close(self,):
        pass
    