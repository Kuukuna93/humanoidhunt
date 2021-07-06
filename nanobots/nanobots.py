from collections import Counter
import re

baseValue = ""

def getMostFrequent(signal):
    c = Counter(signal).most_common(1)
    return c[0][0]
    
def getNextMostFrequent(signal):
    startIndices = [m.start() for m in re.finditer(baseValue[-1:], signal)]
    strings = []
    for i in range(len(startIndices)):
        strings.append(signal[startIndices[i]:startIndices[i]+2])
    return getMostFrequent(strings)

filename = input("Input filename to be parsed:\n")

with open(filename, 'r') as fp:
    signal = fp.read()[0:]
    baseValue = getMostFrequent(signal)

    while(baseValue[-1:] != ";"):
        baseValue = baseValue + getNextMostFrequent(signal)[1]
    
    print(baseValue[0:-1])
