import gym
import os
env = gym.make('CartPole-v0')
perform_record = os.path.join(os.getcwd(), 'cartpole-experiment-1')

env.monitor.start(perform_record)

for i_episode in xrange(20):
    observation = env.reset()
    for t in xrange(100):
        env.render()
        print observation
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print "Episode finished after {} timesteps".format(t+1)
            break

env.monitor.close()