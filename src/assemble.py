import sys
import re

opcodes = {}
regcodes = {}

def loadOpCode(filename):

    opCodeDict = {}

    with open(filename,"r") as opCodeFile:
        for line in opCodeFile:
            splitted = line.split("|")
            opCodeDict[splitted[0]] = splitted[1].strip()

    print("Opcodes loaded. \n")

    return opCodeDict

def loadRegCode(filename):

    regCodeDict = {}

    with open(filename,"r") as regCodeFile:
        for line in regCodeFile:
            splitted = line.split("|")
            regCodeDict[splitted[0]] = splitted[1].strip()

    print("Regcodes loaded. \n")

    return regCodeDict

def getRegister(reg):

    global regcodes

    aux = regcodes.get(reg)

    if aux is None:
        print("Register does not exists. \n")
        sys.exit(0)

    return aux

def decode(line):

    global opcodes

    try:
        commentPosition = line.index(";")
        line = line[:commentPosition-1]
    except ValueError:
        pass

    if re.search('NOP', line):
        return opcodes['NOP']

    elif re.search('HALT', line):
        return opcodes['HALT']

    elif re.search('MOV(\s)*([a-zA-Z]*),(\s)*([a-zA-Z]*)', line):
        line = line.strip()
        regs = line[3:].split(",")
        registers = ""
        for reg in regs:
            registers += getRegister(reg.strip()) + " "
        return opcodes['MOV_RR'] + " " + registers

    elif re.search('MOV(\s)*([a-zA-Z]*),(\s)*(\[[0-9]*\])', line):
        line = line.strip()
        return opcodes["MOV_RM"] + " " + getRegister(line[4:6]) + " " + line[9:len(line) -1]

    elif re.search('MOV(\s)*(\[[0-9]*\]),(\s)*([a-zA-Z]*)', line):
        line = line.strip()
        args = line[4:].split(",")
        return opcodes["MOV_MR"] + " " + (args[0])[1:len(args[0]-1)] + " " + getRegister(args[1])

    elif re.search('MOV(\s)*([a-zA-Z]*),(\s)*([0-9]*)', line):
        line = line.strip()
        args = line[3:].split(",")
        return opcodes['MOV_RI'] + " " + getRegister(args[0]) + " " + args[1]

    elif re.search('MOV(\s)*(\[[0-9]*\]),(\s)*([0-9]*)',line):
        line = line.strip()
        args = line[3:].split(",")
        return opcodes['MOV_MI'] + " " + (args[0])[1:len(args[0]) - 1] + " " + args[1]
    else:
        print("Nao deu boa")
        sys.exit(0)
    return

def main():

    global opcodes

    global regcodes

    opcodes = loadOpCode(sys.argv[2])

    regcodes = loadRegCode(sys.argv[3])


    with open(sys.argv[1], "r") as inputFile:
        for line in inputFile:
            opcode = decode(line)
            print opcode

if __name__ == "__main__":
    main()