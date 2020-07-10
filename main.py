from Domain import *
from MonteCarlo import *
from Walker import *
import matplotlib.pyplot as plt

#Set the domain

#Length Compartment Vector
l=[40*10**-6,20*10**-6]

#DiffusivityVector
D=[1*10**-9,3*10**-9]
P=[0.4*0.001,0.4*0.001]
nPoints=4000

#Domain is set
domain=Domain(l,nPoints,D,P)

domain.createDomain()

#Initialize MonteCarlo Algorithm
algorithm=MonteCarlo(10000)

algorithm.seedWalkersSpecificLocation(20*10**-6,domain)

algorithm.locateWalkers()

initialPositions = algorithm.getWalkerPositions()

#plt.plot(initialPositions, len(initialPositions) * [1], "x")

algorithm.runAlgorithm(0.001,0.00001)

finalPos = algorithm.getWalkerPositions()

finalPos = [x*10**6 for x in finalPos]

dx = [x**2 for x in finalPos]

averageDx2 = av
num_bins = 30

n,bins,patches = plt.hist(finalPos,num_bins,facecolor='blue')

plt.show()

#nP = algorithm.plotNumberOfParticles()

#nP = [(x/10000) for x in nP]

#plt.bar(domain.xCoordinates*10**6,nP)

#plt.show()



#Seed the walkers inside the geometry

