import random


class Animal:
    pass


class Fish(Animal):
    def __str__(self):
        return "F"


class Bear(Animal):
    def __init__(self):
        self.withoutFood = 0

    def __str__(self):
        return 'B'


class Ecosystem:
    def __init__(self, bearDead, bearPercent, fishPercent, lengthRiver, steps):
        self.lengthRiver = lengthRiver
        self.bearNumber = int(0.01 * self.lengthRiver * bearPercent)
        self.fishNumber = int(0.01 * self.lengthRiver * fishPercent)
        self.noneNumber = self.lengthRiver - (self.bearNumber + self.fishNumber)
        self.steps = steps
        self.river = []
        self.bearDead = bearDead
        self.__life()

    def __str__(self):
        for i in range(self.lengthRiver):
            if self.river[i] is None:
                print('_', end=' ')
            else:
                print(self.river[i].__str__(), end=' ')

    def __life(self):
        self.__filling()
        if self.steps > 0:
            for i in range(self.steps):
                if self.fishNumber == self.lengthRiver or self.bearNumber == self.lengthRiver:
                    break
                print()
                self.__stepLife()
        else:
            s = ''
            while s != 'stop' and self.fishNumber != self.lengthRiver and self.bearNumber != self.lengthRiver:
                self.__stepLife()
                s = input()

    def __filling(self):
        for i in range(self.bearNumber):
            self.river.append(Bear())
        for i in range(self.fishNumber):
            self.river.append(Fish())
        for i in range(self.fishNumber + self.bearNumber, self.lengthRiver):
            self.river.append(None)
        self.__shuffle()

    def __shuffle(self):
        shuffleList = []
        while len(self.river) != 0:
            i = random.randint(0, len(self.river) - 1)
            shuffleList.append(self.river.pop(i))
        self.river = shuffleList

    def __stepLife(self):
        nextStep = -1
        for i in range(0, len(self.river)):
            if nextStep == -1:
                if type(self.river[i]) == Bear:
                    nextStep = self.__moveBear(i)
                if type(self.river[i]) == Fish:
                    nextStep = self.__moveFish(i)
            else:
                nextStep = -1
        self.__str__()

    def __moveBear(self, i):
        x = self.river[i].withoutFood
        step = self.getStep(i, self.lengthRiver)
        if type(self.river[i + step]) == Fish:
            self.river[i] = None
            self.fishNumber -= 1
            self.noneNumber += 1
            self.river[i + step] = Bear()
        elif type(self.river[i + step]) == Bear:
            self.__newAnimal('bear')
            if x == self.bearDead - 1:
                self.river[i] = None
                self.bearNumber -= 1
                self.noneNumber += 1
                return
            self.river[i].withoutFood += 1
            return -1
        else:
            self.river[i] = None
            if x == self.bearDead - 1:
                self.bearNumber -= 1
                self.noneNumber += 1
                return
            self.river[i + step] = Bear()
            self.river[i + step].withoutFood = x + 1
        return step

    def __moveFish(self, i):
        step = self.getStep(i, self.lengthRiver)
        if type(self.river[i + step]) == Bear:
            self.river[i] = None
            self.noneNumber += 1
            self.fishNumber -= 1
            self.river[i + step].withoutFood = 0
            return -1
        elif type(self.river[i + step]) == Fish:
            self.__newAnimal('fish')
            return -1
        else:
            self.river[i] = None
            self.river[i + step] = Fish()
        return step

    @staticmethod
    def getStep(i, lengthRiver):
        if i == 0:
            return 1
        elif i == lengthRiver - 1:
            return -1
        else:
            return -1 if random.randint(0, 1) == 0 else 1

    def __newAnimal(self, obj):
        index = self.__getNewIndex()
        if index != -1:
            self.river[index] = Bear() if obj == 'bear' else Fish()
            self.noneNumber -= 1
            if obj == 'bear':
                self.bearNumber += 1
            else:
                self.fishNumber += 1

    def __getNewIndex(self):
        if self.noneNumber != 0:
            item = random.randint(1, self.noneNumber)
            number = 0
            for i in range(self.lengthRiver):
                if self.river[i] is None:
                    number += 1
                    if number == item:
                        return i
        else:
            return -1


print('Введите значения:')
lengthRiver = int(input('Длинна реки: '))
deadBear = int(input('Число шагов медведя без еды: '))
bear = int(input("Процент медведей в реке: "))
fish = int(input('Процент рыбы в реке: '))
steps = int(input('Число кругов жизни (0 для ручного управления): '))
if steps == 0:
    print('Для показа следующего круга нажмите Enter, для завершения введите "stop"')
e = Ecosystem(deadBear, bear, fish, lengthRiver, steps)
