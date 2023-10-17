import gym
import numpy as np

env = gym.make("Taxi-v3", render_mode="human")
env.reset(seed=4200)

moveset = [3,3,3,3,3,3,3,1,1,4,0,0,2,2,2,2,2,2,2,1,1,5]

for x in moveset:
    action = x
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        env.reset()
env.close()

# Action Space: Discrete
# Observation Space: Discrete