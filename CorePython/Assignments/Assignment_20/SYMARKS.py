class SYMARKS:

    def __init__(self, computerTotal, mathsTotal, electronicsTotal):
        self.computerTotal = computerTotal
        self.mathsTotal = mathsTotal
        self.electronicsTotal = electronicsTotal

    # Getters
    def getComputerTotal(self):
        return self.computerTotal

    def getMathsTotal(self):
        return self.mathsTotal

    def getElectronicsTotal(self):
        return self.electronicsTotal

    # Setters
    def setComputerTotal(self, computerTotal):
        self.computerTotal = computerTotal

    def setMathsTotal(self, mathsTotal):
        self.mathsTotal = mathsTotal

    def setElectronicsTotal(self, electronicsTotal):
        self.electronicsTotal = electronicsTotal