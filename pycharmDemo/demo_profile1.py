__author__ = 'Marc-Andre Gardner'

import pickle

def getData():
    return pickle.load(open('dataprofile.pkl', 'rb'))

class CorrespondanceChecker:

    def __init__(self, compList):
        self.compData = set(compList)
        self.reset()

    def reset(self):
        self.presenceData = []
        self.countFound = 0

    def _testIfContains(self, elem):
        return elem in self.compData

    def _addItem(self, elem, ispresent):
        for i, (val, present) in enumerate(self.presenceData):
            if val == elem:
                self.presenceData[i] = (val, self.presenceData[i][1] | ispresent)
                break
        else:
            self.presenceData.append((elem, ispresent))
        self.countFound += 1 if ispresent else 0

    def check(self, inputList):
        for val in inputList:
            self._addItem(val, self._testIfContains(val))
        return self.presenceData


if __name__ == '__main__':
    bigL, smallL = getData()

    c = CorrespondanceChecker(bigL)
    r = c.check(smallL)

































        #from collections import defaultdict
        # self.presenceData = defaultdict(bool)
        #self.presenceData[elem] |= ispresent