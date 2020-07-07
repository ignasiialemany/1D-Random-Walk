from Domain import *
from MonteCarlo import *
from Walker import *

#Set the domain

#Length Vector
l=[0.5,2,0.25,3,0.1,4,0.5]

#DiffusivityVector
D_extraCell=1
D_insideCell=3
D=[1,3,1,3,1,3,1]
P=[5*10**-2]*len(l)
nPoints=100

#Domain is set
domain=Domain(l,nPoints,D,P)

domain.createDomain()

#Initialize MonteCarlo Algorithm
algorithm=MonteCarlo(100)

algorithm.seedWalkersInGeometry(domain)

algorithm.locateWalkers()

#Seed the walkers inside the geometry

