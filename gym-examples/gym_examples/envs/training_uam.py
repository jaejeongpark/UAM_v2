# from wrappers import airspace, airtrafficcontroller
import uam_uav
import gymnasium as gym
# import stable_baselines3 as sb3 



# env = gym.make('CartPole-v1') #enter string name of uam_env after registering 
# observation, info = env.reset()
location_name = 'Austin, Texas, USA'
num_vertiport = 15
num_reg_uav = 10
# sim sleep time
sleep_time = 0.03
#sim run time
total_timestep = 1000

env = uam_uav.Uam_Uav_Env(location_name,num_vertiport,num_reg_uav,render_mode="Human")
observation, info = env.reset()

for _ in range(1000):
    action = env.action_space.sample()  # agent policy that uses the observation and info
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()

env.close()

