import gym
env = gym.make('CartPole-v0')
for i_episode in xrange(5):
    observation = env.reset()
    for t in xrange(100):
        env.render()
        print observation
        action = env.action_space.sample()
        """
        observation (object) : an environment-specific object
                               representing your observation
                               of the environment
        reward (float)       : amount of reward achieved by the previous
                               action
        done (boolean)       : whether it's time to reset environment
                               again
        info (dict)          : diagnostic information useful for debugging
        """
        observation, reward, done, info = env.step(action)
        if done:
            print "Episode finished after {} timesteps".format(t+1)
            break