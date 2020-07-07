#This class will contain all the information related to walkers inside the 1D domain. It will contain the position,
# phase and flag for each walker.

import numpy as np

class Walker:

    def __init__(self):
        self.position=0
        self.index=0
        self.dx = 0

    def defineStep(self,dx):
        self.dx=dx

    def stepWalker(self):
        return np.random.uniform(-self.dx,self.dx)

    def transitProbability(self):
        return np.random.uniform(0,1)





