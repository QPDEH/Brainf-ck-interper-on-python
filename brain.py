from sys import argv, stdout
inputtext = open(argv[1], "r").read()
ribbon = []
for i in range(30000): ribbon.append(0)
stack = []
i = 0
lettern = -1
try:
    while True:
        lettern += 1
        if inputtext[lettern] == "+": ribbon[i] += 1
        elif inputtext[lettern] == "-": ribbon[i] -= 1
        elif inputtext[lettern] == ">": i += 1
        elif inputtext[lettern] == "<": i -= 1
        elif inputtext[lettern] == ".": stdout.write(chr(ribbon[i]))
        elif inputtext[lettern] == ",":
            input_ = input()
            deep = 0
            for inputletter in input_:
                ribbon[i] = ord(inputletter)
                i += 1
                deep += 1
            i -= deep
        elif inputtext[lettern] == "[":
            if not ribbon[i] == 0:
                stack.append(lettern)
        elif inputtext[lettern] == "]":
            if not ribbon[i] == 0:
                lettern = stack[-1]
            else: stack = stack[:-1]
        if lettern == len(inputtext) - 1: break
except Exception as ex: print(f"Interpreter exception\n{ex}")
