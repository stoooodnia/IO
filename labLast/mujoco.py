import gym

# Inicjalizacja środowiska
env = gym.make('Swimmer-v4', render_mode='human')

observation, info = env.reset(seed=42)

for _ in range(60):
   action = env.action_space.sample()
   observation, reward, terminated, truncated, info = env.step(action)

   if terminated or truncated:
      observation, info = env.reset()
env.close()

# Action Space: Continuous 
# Observation Space: Continuous
