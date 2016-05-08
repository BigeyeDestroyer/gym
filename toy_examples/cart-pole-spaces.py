from gym import spaces
space = spaces.Discrete(8)  # set with 8 elements {0, 1, 2, ..., 7}
x = space.sample()
assert space.contains(x)
assert space.n == 8
print x