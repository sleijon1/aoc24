def combo_operand(operand, registers):
    if operand == 4:
        return registers["A"]
    elif operand == 5:
        return registers["B"]
    elif operand == 6:
        return registers["C"]
    return operand

def adv(operand, registers):
    registers["A"]  = registers["A"] // 2**combo_operand(operand, registers)

def bxl(operand, registers):
    registers["B"] = registers["B"] ^ operand

def bst(operand, registers):
    registers["B"] = combo_operand(operand, registers) % 8

def jnz(operand, registers):
    return registers["A"] != 0

def bxc(operand, registers):
    registers["B"] = registers["B"] ^ registers["C"]

def out(operand, registers, output):
    output.append(combo_operand(operand, registers) % 8)

def bdv(operand, registers):
    registers["B"] = registers["A"] // 2**combo_operand(operand, registers)

def cdv(operand, registers):
    registers["C"] = registers["A"] // 2**combo_operand(operand, registers)



def execute_instruction(instructions, registers, output=[]):
    pointer = 0
    ops = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

    while pointer < len(instructions):
        instruction = instructions[pointer]
        if instruction == 5:
            ops[instruction](instructions[pointer+1], registers, output)
        else:
            val = ops[instruction](instructions[pointer+1], registers)
        if instruction == 3 and val:
            pointer = instructions[pointer+1]
            continue
        pointer += 2

    return ','.join(map(str, output))

def part_one():
    registers = {"A": 27334280, "B": 0, "C": 0}
    instructions = [2,4,1,2,7,5,0,3,1,7,4,1,5,5,3,0] 
    print(f"part 1: {execute_instruction(instructions, registers)}")

def part_two():
    instructions = [2,4,1,2,7,5,0,3,1,7,4,1,5,5,3,0]
    initial = 0
    while True:
        registers = {"A": initial, "B": 0, "C": 0}
        if (_out := execute_instruction(instructions, registers, output=[])) == ','.join(map(str, instructions)):
            print(f"part 2: {initial}")
            break
        print(f"trying {initial} -> {_out}")
        initial += 1

def part_two_w():
    instructions = [2,4,1,2,7,5,0,3,1,7,4,1,5,5,3,0]
    initial = 27334280
    while True:
        output = []
        A = initial
        i = 0
        while A:
            #y = 
            # (A % 8 ^ 2) 0 to 7
            # 2**(0 to 7)
            # 
            e = ((A // 2**(A % 8 ^ 2)) ^ (A % 8 ^ 2) ^ 7) % 8
            output.append(e)
            
            A = A // 2**3
            print("output", e % 8)
            i += 1
        print(f"part 2: {','.join(map(str, output))}")
        break
        if ','.join(map(str, output)) == ','.join(map(str, instructions)):
            print(f"part 2: {initial}")
            break
        initial += 1
        

part_one()#
#part_two()
part_two_w()
