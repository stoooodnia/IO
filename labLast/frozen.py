import gym
import numpy as np 
    
env = gym.make('FrozenLake8x8-v1', render_mode="human")
env.reset(seed=42)

moveset = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1]
for x in moveset:
   action = x
   observation, reward, terminated, truncated, info = env.step(action)

   if terminated or truncated:
      observation, info = env.reset()
env.close()


# 