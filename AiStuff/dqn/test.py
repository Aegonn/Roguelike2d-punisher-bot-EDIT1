import sys
import random
from dqn import Agent
import numpy as np


class MockEnv:
    def __init__(self, env_name):
        self.action_space = MockActionSpace(10)
        self.observation_space = MockObservationSpace((1, 1, 1))

    def reset(self):
        return self.random_observation()

    def step(self, action):
        print("stepping")
        return self.random_observation(), 5, random.randint(0, 1000) == 555, None

    def random_observation(self):
        return np.zeros((1, 1, 1, 1))
        #return [[0] * 12]

class MockActionSpace:
    def __init__(self, n):
        self.n = n

class MockObservationSpace:
    def __init__(self, shape):
        self.shape = shape

num_episodes = 20

env_name = sys.argv[1] if len(sys.argv) > 1 else "MsPacman-v0"
env = MockEnv(env_name)

agent = Agent(state_size=env.observation_space.shape,
              number_of_actions=env.action_space.n,
              save_name=env_name)

for e in range(num_episodes):
    observation = env.reset()
    done = False
    agent.new_episode()
    total_cost = 0.0
    total_reward = 0.0
    frame = 0
    while not done:
        frame += 1
        #env.render()
        action, values = agent.act(observation)
        print(action)
        #action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        total_cost += agent.observe(reward)
        total_reward += reward
    print("total reward {}".format(total_reward))
    print("mean cost {}".format(total_cost/frame))