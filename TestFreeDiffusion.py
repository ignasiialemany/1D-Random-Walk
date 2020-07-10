from Domain import *
from MonteCarlo import *
import matplotlib.pyplot as plt

#Length Compartment Vector
l=[40*10**-6]
D=[1*10**-9]
P=[0.4*0.001]
nPoints=4000

domain= Domain(l,nPoints,D,P)
domain.createDomain()
epsilon=[]
walkers = [100000]

for i in range (0,len(walkers)):
    # Number of Particles, seeding and location of walkers
    algorithm = MonteCarlo(walkers[i])
    algorithm.seedWalkersSpecificLocation(20 * 10 ** -6, domain)
    algorithm.locateWalkers()

    # Run Algorithm
    initialPosition = algorithm.getWalkerPositions()
    algorithm.runAlgorithm(0.001,1e-06)
    finalPosition = algorithm.getWalkerPositions()

    dx = [(x - 20 * 10 ** -6) ** 2 for x in finalPosition]

    averageDx2 = sum(dx) / len(dx)

    epsilon.append(abs(averageDx2 - 2 * D[0] * 0.000001))
    num_bins = [15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 25]
    finalPosition = [x * 10 ** 6 for x in finalPosition]

    plt.figure()
    plt.title("walkers={}, dt=1e-06".format(walkers[i]))
    n, bins, patches = plt.hist(finalPosition, num_bins)
    plt.savefig("plot_walkers={}.png".format(walkers[i]))
    plt.close()
    print(averageDx2)

plt.figure()
plt.plot(walkers,epsilon)
plt.show()

