#This class will run the main algorithm.

from Walker import *
import random


class MonteCarlo:

    def __init__(self,nP):
        self.particles=[]
        self.nP=nP
        #Init the number of particles
        for i in range (self.nP):
            self.particles.append(Walker())

    #This function will seed the walkers inside the 1D domain.
    def seedWalkersInGeometry(self,domain):
        self.domain = domain
        for i in range(len(self.particles)):
            self.particles[i].position = (random.random()*domain.length) + domain.xCoordinates[0]

    def locateWalkers(self):
        #Locate walkers inside the domain
        #Total Complexity O(numberParticles*numberOfBarriers)
        for i in range(len(self.particles)):
            pos = self.particles[i].position
            closestBarrier = min(self.domain.barriers_position, key=lambda x :abs(x-pos)) #O(n) could be improved to O(lgN) with binary search
            if (pos>closestBarrier):
                self.particles[i].index = list(self.domain.barriers_position).index(closestBarrier)
            else:
                self.particles[i].index = list(self.domain.barriers_position).index(closestBarrier) - 1












