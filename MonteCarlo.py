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



    def locateIndex(self,pos):
        closestBarrier = min(self.domain.barriers_position, key=lambda x :abs(x-pos)) #O(n) could be improved to O(lgN) with binary search
        if (pos>closestBarrier):
            return list(self.domain.barriers_position).index(closestBarrier)
        else:
            return list(self.domain.barriers_position).index(closestBarrier) - 1

    def locateWalkers(self):
        #Locate walkers inside the domain
        #Total Complexity O(numberParticles*numberOfBarriers)
        for i in range(len(self.particles)):
            pos = self.particles[i].position
            self.particles[i].index = self.locateIndex(pos)

    def runAlgorithm(self,dt):



    def allWalkersOneStep(self):
        for i in range (len(self.particles)):

            self.particles[i].defineStep(self.domain, self.domain.dx)
            pos = self.particles[i].position
            indexCell = self.particles[i].index
            D = self.domain.diffusivity[indexCell]
            P = self.domain.permeability[indexCell]
            s = self.particles[i].stepWalker()

            newIndex = self.locateIndex(s+pos)

            if(newIndex!=indexCell):
                transit_probability = self.particles[i].transitProbability()
                cross_probability =


            else:
                #update position and follow to the next step














