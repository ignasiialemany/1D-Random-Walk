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

    def createDomain(self):
        #Coordinates in x
        self.xCoordinates = np.linspace(0, self.length, self.nPoints)
        self.indexBarriers = np.concatenate((np.zeros(1), np.round((self.nPoints) * np.cumsum(self.lengthVector) / self.length)))
        self.barriers_position = self.indexBarriers * (self.length / (self.nPoints - 1))
        self.lengthVector = np.diff(self.barriers_position)
        self.numberOfCompartments = len(self.lengthVector)
