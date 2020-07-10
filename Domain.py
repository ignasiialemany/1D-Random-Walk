#This is a class that will contain the 1D geometry.
import numpy as np

class Domain:

    def __init__(self,lengths,nPoints,diffusivities,permeability):
        self.lengthVector = lengths
        self.length = sum(lengths)
        self.nPoints=nPoints
        self.diffusivity = diffusivities
        self.permeability = permeability

        #When creating the domain those are computed
        self.xCoordinates=[]
        self.indexBarriers=[]
        self.barriers_position=[]
        self.numberOfCompartments = 0
        self.dx=0

    def createDomain(self):
        #Coordinates in x
        self.barriers_position = np.concatenate((np.zeros(1), np.cumsum(self.lengthVector)))
        self.numberOfCompartments = len(self.lengthVector)
