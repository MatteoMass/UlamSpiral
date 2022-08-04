import numpy as np
import math
import matplotlib.pyplot as plt        
        

class UlamSpiral:
    
    UlamMatrix = None
    PrimeUlamMatrix = None
    counterclockwise = True
    size = None
    rotation = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    walker = None

    def __init__(self, size, counterclockwise = False):
        if size % 2 == 0:
            size = size +1

        self.UlamMatrix = np.empty((size, size))
        self.PrimeUlamMatrix = np.empty((size, size))

        self.counterclockwise = counterclockwise
        if self.counterclockwise:
            self.rotation.reverse()
        self.size = size
        self.walker = (int((self.size-1)/2), int((self.size-1)/2))

    def isInMatrix(self):
        if self.walker[0] < 0 or self.walker[0] > (self.size -1):
            print("a")
            return False
        if self.walker[1] < 0 or self.walker[1] > (self.size -1):
            return False
        return True
         
    def createSimpleSpiral(self):
        goOn = True
        i = 1
        j = 0

        while goOn:
            self.UlamMatrix[self.walker[0]][self.walker[1]] = i
            i = i+1
            self.walker = np.add(self.walker, self.rotation[j])
            if not self.isInMatrix():
                goOn = False
            else:
                k = (j + 1)%4
                x, y = np.add(self.walker, self.rotation[k])
                if self.UlamMatrix[x][y] == 0:
                    j = k

    def isPrime(self, n):
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return 0
        return 1
                

    def createSpiral(self):
        goOn = True
        i = 1
        j = 0

        while goOn:
            self.UlamMatrix[self.walker[0]][self.walker[1]] = i
            self.PrimeUlamMatrix[self.walker[0]][self.walker[1]] = self.isPrime(i)
            i = i+1
            self.walker = np.add(self.walker, self.rotation[j])
            if not self.isInMatrix():
                goOn = False
            else:
                k = (j + 1)%4
                x, y = np.add(self.walker, self.rotation[k])
                if self.UlamMatrix[x][y] == None:
                    j = k

    def getUlamMatrix(self):
        for i in range(self.UlamMatrix.shape[0]):
            for j in range(self.UlamMatrix.shape[1]):
                print(self.UlamMatrix[i][j].number, end= ' ')
            print("\n")
        pass

    def getUlamMatrix2(self):
        for i in range(self.UlamMatrix.shape[0]):
            for j in range(self.UlamMatrix.shape[1]):
                print(self.UlamMatrix[i][j].isPrime, end= ' ')
            print("\n")
        pass


if __name__ == "__main__":
    us = UlamSpiral(5)
    us.createSpiral()
    plt.imshow(us.PrimeUlamMatrix, cmap='Greys',  interpolation='nearest')