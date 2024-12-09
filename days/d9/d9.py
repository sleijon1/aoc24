line = open("input.txt").read().strip()

# parse the string
# map empty space to a list of indicies which we pop from when moving memory back


free_space_queue = []
memory = []
memory_int = 0
for i, char in enumerate(line):
    if i % 2 == 1:
        for j in range(int(char)):
            memory.append(".")
            free_space_queue.append(len(memory)-1)
    else:
        for j in range(int(char)):
            memory.append(str(memory_int))
        memory_int += 1
#print("freespacequeue", free_space_queue)
#print("memory", memory)

while free_space_queue:
    i = free_space_queue.pop(0)
    print("freespacequeue", free_space_queue)
    if all(el == '.' for el in memory [i:]): #cheesy, change
        break
    mem_i = -1
    while memory[mem_i] == ".": 
        mem_i -= 1
    #print("i", i, "dig", mem_i)
    memory[i] = memory[mem_i]
    memory[mem_i] = "."

    print("memory", memory)
    print("freespacequeue", free_space_queue)

checksum = 0
for id in range(0, len(memory)):
    if memory[id] != ".":
        checksum += id*int(memory[id])

print(f"p1: {checksum}")