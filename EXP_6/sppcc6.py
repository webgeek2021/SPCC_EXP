results = [] 
registors = []
arg1 = [] 
arg2 = []
opcodes = []
lines_of_codes = 0

def find_reg(operand):
    for index in range(len(registors)):
        if registors[index] == operand:
            return index
    
    return -1

def get_ins(expression):
    if(expression == "+"):
        return "ADD"
    return "SUB"
    

def gen_reg():
    return len(registors)


with open("./EXP_6/input.txt","r") as file:

    for line in file:
        # print(line.rstrip().split(" "))
        l =line.rstrip().split(" ")

        results.append(l[0])
        arg1.append(l[2])

        if(len(l) > 3):
            arg2.append(l[4])
            opcodes.append(l[3])
        else :
            arg2.append(None)
            opcodes.append(None)
        lines_of_codes += 1

code = ""
for i in range(lines_of_codes):
    if(opcodes[i]):
        temp1 = find_reg(arg1[i])
        temp2 = find_reg(arg2[i])

        if(temp1 == -1 and temp2 == -1):
            tempReg = gen_reg()
            code += f'MOV {arg1}, R{tempReg}\n'
            registors.append(results[i])
        
        elif not temp1 == -1 and not temp2 == -1 :
            code += f"{get_ins(opcodes[i])} R{temp1} , R{temp2}\n"
            registors[temp2] = results[i]
        
        else:
            temp1 = find_reg(arg1)
            if not temp1 == -1:
                code += f"MOV R{temp1} , {results[i]} \n"
            else:
                tempReg = gen_reg()
                code += f"MOV {arg1[i]} , R{tempReg} \n"
                code += f"MOV R{tempReg} , {results[i]}"


print(code)


