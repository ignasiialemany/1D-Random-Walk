#This class will contain all the information related to walkers inside the 1D domain. It will contain the position,
# phase and flag for each walker.

import numpy as np

class Walker:

    def __init__(self):
        self.position=0
        self.index=0

    def stepWalker(self,diffusivity, dt):
        step = np.random.normal(0,1)
        step = step * np.sqrt(diffusivity*2*dt)
        return step

    def transitProbability(self):
        return np.random.uniform(0,1)





