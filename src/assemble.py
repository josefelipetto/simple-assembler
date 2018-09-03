import sys
import file

def loadOpCode():
    print("Load Op Code")

def loadRegCode():
    print("Load Reg Code")

def decode(line):
    return

def main():
    with open(sys.argv[0],"r") as inputFile:
        for line in inputFile:
            opcode = decode(line)