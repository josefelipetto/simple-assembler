#!/usr/bin/env python
import sys
import re

opcodes = {}
regcodes = {}

def loadOpCode(filename):

    opCodeDict = {}

    with open(filename, "r") as opCodeFile:
        for line in opCodeFile:
            splitted = line.split("|")
            opCodeDict[splitted[0]] = splitted[1].strip()

    print("Opcodes loaded. \n")

    return opCodeDict

def loadRegCode(filename):

    regCodeDict = {}

    with open(filename, "r") as regCodeFile:
        for line in regCodeFile:
            splitted = line.split("|")
            regCodeDict[splitted[0]] = splitted[1].strip()

    print("Regcodes loaded. \n")

    return regCodeDict

def getRegister(reg):

    global regcodes

    aux = regcodes.get(reg)

    if aux is None:
        print("Register " + reg + " does not exists. \n")
        sys.exit(0)

    return aux

def decode(line):

    global opcodes

    try:
        commentPosition = line.index(";")
        line = line[:commentPosition]
    except ValueError:
        pass

    if line.strip() == "":
        return ""

    if re.search(r'NOP', line):
        return opcodes['NOP']

    elif re.search(r'HALT', line):
        return opcodes['HALT']

    elif re.search(r'MOV(\s)*([a-zA-Z]+)(\s)*,(\s)*(\[[0-9]+\])(\s)*', line):
        line = re.sub("(\s)*", "", line)
        return opcodes["MOV_RM"] + " " + getRegister(line[3:5]) + " " + line[7:len(line) - 1]

    elif re.search(r'MOV(\s)*([a-zA-Z]+)(\s)*,(\s)*([a-zA-Z]+)(\s)*', line):
        line = re.sub("(\s)*", "", line)
        regs = line[3:].split(",")
        return opcodes['MOV_RR'] + " " + getRegister(regs[0]) + " " + getRegister(regs[1])

    elif re.search(r'MOV(\s)*(\[[0-9]+\])(\s)*,(\s)*([a-zA-Z]+)(\s)*', line):
        line = line.strip()
        args = line[4:].split(",")
        return opcodes["MOV_MR"] + " " + (args[0])[1:len(args[0])-1] + " " + getRegister(args[1])

    elif re.search(r'MOV(\s)*([a-zA-Z]+)(\s)*,(\s)*([-])?(\s)*([0-9]+)(\s)*', line):
        line = re.sub(r"(\s)*", "", line)
        args = line[3:].split(",")
        return opcodes['MOV_RI'] + " " + getRegister(args[0]) + " " + args[1]

    elif re.search(r'MOV(\s)*(\[[0-9]+\])(\s)*,(\s)*([-])?(\s)*([0-9]+)(\s)*', line):
        line = re.sub(r"(\s)*", "", line)
        args = line[3:].split(",")
        return opcodes['MOV_MI'] + " " + (args[0])[1:len(args[0]) - 1] + " " + args[1]

    elif re.search(r'ADD(\s)*([a-zA-Z]+)(\s)*,(\s)*([a-zA-Z]+)(\s)*', line):
        line = line.strip()
        regs = line[3:].split(",")
        return opcodes['ADD'] + " " + getRegister(regs[0].strip()) + " " + getRegister(regs[1].strip())

    elif re.search(r'SUB(\s)*([a-zA-Z]+)(\s)*,(\s)*([a-zA-Z]+)(\s)*', line):
        line = line.strip()
        regs = line[3:].split(",")
        return opcodes['SUB'] + " " + getRegister(regs[0].strip()) + " " + getRegister(regs[1].strip())

    elif re.search(r'CMP(\s)*([a-zA-Z]+)(\s)*,(\s)*([a-zA-Z]+)(\s)*', line):
        line = line.strip()
        regs = line[3:].split(",")
        return opcodes['CMP'] + " " + getRegister(regs[0].strip()) + " " + getRegister(regs[1].strip())

    elif re.search(r'JMP(\s)*([0-9]+)', line):
        line = line.strip()
        return opcodes['JMP'] + " " + (line.split(" "))[1]

    elif re.search(r'JZ(\s)*([-])?(\s)*([-])?([0-9]+)', line):
        line = re.sub(r"(\s)*", "", line)
        return opcodes['JZ'] + " " + line[2:]

    elif re.search(r'JG(\s)*([-])?([0-9]+)', line):
        line = re.sub(r"(\s)*", "", line)
        return opcodes['JG'] + " " + line[2:]

    elif re.search(r'JL(\s)*([-])?([0-9]+)(\s)*', line):
        line = re.sub(r"(\s)*", "", line)
        return opcodes['JL'] + " " + line[2:]

    elif re.search(r'OUT(\s)*([a-zA-Z]+)(\s)*', line):
        line = line.strip()
        args = re.sub(r"OUT(\s)*", "", line)

        return opcodes['OUT'] + " " + getRegister(args)

    elif re.search(r'INC(\s)*([a-zA-Z]+)(\s)*', line):
        line = line.strip()
        args = re.sub(r"INC(\s)*","",line)

        return opcodes['INC'] + " " + getRegister(args)

    elif re.search(r'DEC(\s)*([a-zA-Z]+)(\s)*', line):
        line = line.strip()
        args = re.sub(r"DEC(\s)*","",line)

        return opcodes['DEC'] + " " + getRegister(args)

    elif re.search(r'MUL(\s)*([a-zA-Z]+)(\s)*,(\s)*([a-zA-Z]+)(\s)*', line):
        line = line.strip()
        line = re.sub(r"MUL(\s)*","",line)
        regs = line.split(",")
        return opcodes['MUL'] + " " + getRegister(regs[0].strip()) + " " + getRegister(regs[1].strip())

    elif re.search(r'DIV(\s)*([a-zA-Z]+)(\s)*,(\s)*([a-zA-Z]+)(\s)*', line):
        line = line.strip()
        line = re.sub(r"DIV(\s)*", "", line)
        regs = line.split(",")
        return opcodes['DIV'] + " " + getRegister(regs[0].strip()) + " " + getRegister(regs[1].strip())

    else:
        print("Command " + line.strip() + " not found")
        sys.exit(0)

    return

def main():

    global opcodes

    global regcodes

    opcodes = loadOpCode(sys.argv[2])

    regcodes = loadRegCode(sys.argv[3])

    output = ""

    with open(sys.argv[1], "r") as inputFile:
        for line in inputFile:
            opcode = decode(line)
            if opcode != "":
                output += opcode + " "

    print output

    outputfile = open("bin/" + sys.argv[4], "w") if re.search('([a-zA-Z]+).run', sys.argv[4]) else open("bin/" + sys.argv[4] + ".run", "w")

    outputfile.write(output)


if __name__ == "__main__":
    main()
