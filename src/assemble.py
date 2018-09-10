import sys
import file
import re

def loadOpCode(filename):

    opCodeDict = {}

    with open(filename,"r") as opCodeFile:
        for line in opCodeFile:
            splitted = line.split("|")
            for split in splitted:
                opCodeDict[split[0]] = split[1]

    print("Opcodes loaded. \n")

    return opCodeDict

def loadRegCode(filename):

    regCodeDict = {}

    with open(filename,"r") as regCodeFile:
        for line in regCodeFile:
            splitted = line.split("|")
            for split in splitted:
                regCodeDict[split[0]] = split[1]

    print("Regcodes loaded. \n")

    return regCodeDict

def decode(line):
    return

def main():

    opcodes = loadOpCode(sys.argv[1])

    regcodes = loadRegCode(sys.argv[2])

    with open(sys.argv[0],"r") as inputFile:
        for line in inputFile:
            opcode = decode(line)