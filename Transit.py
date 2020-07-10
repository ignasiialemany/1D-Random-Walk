
class Transit:

    def __init__(self):
        self.a = 0

    @staticmethod
    def FieremansProbability(dx, P, D):
        term = 2 * dx * P / D
        probability = term / (1 + term)
        return probability
