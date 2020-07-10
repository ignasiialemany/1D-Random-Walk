# This class will run the main algorithm.

from Walker import *
from Domain import *
from Transit import *
import numpy as np

class MonteCarlo:

    def __init__(self, nP):
        self.particles = []
        self.nP = nP
        # Init the number of particles
        for i in range(self.nP):
            self.particles.append(Walker())

    # This function will seed the walkers inside the 1D domain.
    def seedWalkersInGeometry(self, domain):
        self.domain = domain
        for i in range(len(self.particles)):
            self.particles[i].position = (np.random.uniform(0, 1) * domain.length) + domain.xCoordinates[0]

    def locateIndex(self, pos):
        closestBarrier = min(self.domain.barriers_position,
                             key=lambda x: abs(x - pos))  # O(n) could be improved to O(lgN) with binary search
        if pos > closestBarrier:
            return list(self.domain.barriers_position).index(closestBarrier)
        else:
            return list(self.domain.barriers_position).index(closestBarrier) - 1

    def locateWalkers(self):
        # Locate walkers inside the domain
        # Total Complexity O(numberParticles*numberOfBarriers)
        for i in range(len(self.particles)):
            pos = self.particles[i].position
            self.particles[i].index = self.locateIndex(pos)

    def seedWalkersSpecificLocation(self,x0,domain):
        self.domain = domain
        for i in range(len(self.particles)):
            self.particles[i].position=x0

    def runAlgorithm(self, T,dT):
        time=0
        while(time<=T):
            self.allWalkersOneStep(dT)
            time += dT
            #self.checkWalkersLocation(20*10**-6)
            if (time > T):
                print(time)
                self.allWalkersOneStep(time-T)
                break


    def checkWalkersLocation(self,x0):
        counterRight=0
        counterLeft=0
        counterx0=0
        for i in range(len(self.particles)):
            dx = (self.particles[i].position-x0)
            if(dx>0):
                counterRight+=1
            elif(dx<0):
                counterLeft+=1
            else:
                counterx0+=1
        x=5

    def allWalkersOneStep(self,dt):

        # 1 - Walkers that go out of the boundaries. Should I reflect them into the domain or create a buffer?
        for i in range(len(self.particles)):
            pos = self.particles[i].position
            indexCell = self.particles[i].index
            if(indexCell > self.domain.numberOfCompartments):
                x=3
            D = self.domain.diffusivity[indexCell]
            P = self.domain.permeability[indexCell]
            s = self.particles[i].stepWalker(D, dt)
            newIndex = self.locateIndex(s + pos)
            if (abs(indexCell - newIndex) > 1):
                x = 5
            if(newIndex == -1):
                x = 7
            crosses = False
            if newIndex != indexCell:
                walker_transit_probability = self.particles[i].transitProbability()
                transit_model = Transit()
                distance_pos_to_barrier = self.domain.barriers_position[indexCell] - pos
                distance_barrier_to_target = (s + pos) -  self.domain.barriers_position[indexCell]
                probability_crossing = transit_model.FieremansProbability(distance_pos_to_barrier, P, D)
                if probability_crossing == 1:
                    crosses = True
                elif probability_crossing == 0:
                    crosses = False
                else:
                    crosses = walker_transit_probability <= probability_crossing

                if(crosses==True):
                    self.particles[i].index = newIndex
                    self.particles[i].position = s + pos
                else:
                    self.particles[i].index = indexCell
                    self.particles[i].position = self.domain.barriers_position[indexCell] - distance_barrier_to_target
            else:
                self.particles[i].index = indexCell
                self.particles[i].position = s + pos


    def getWalkerPositions(self):
        finalPositions = []
        for i in range (len(self.particles)):
            finalPositions.append(self.particles[i].position)
        return finalPositions


    def plotNumberOfParticles(self):
        numberOfParticles = [0]*len(self.domain.xCoordinates)
        for i in range(len(self.particles)):
            finalPos = self.particles[i].position
            closestXCoord = min(self.domain.xCoordinates,key=lambda x: abs(x - finalPos))  # O(n) could be improved to O(lgN) with binary search
            index = list(self.domain.xCoordinates).index(closestXCoord)
            numberOfParticles[index] += 1
        return numberOfParticles