from collections import defaultdict
line = open("input.txt").read().strip()


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

memlen = len(memory)
moved = defaultdict(bool)

free_chunks = []
current_chunk = []
for i in range(len(free_space_queue)):
    if i == 0 or free_space_queue[i] == free_space_queue[i-1]+1:
        current_chunk.append(free_space_queue[i])
    else:
        free_chunks.append(current_chunk)
        current_chunk = [free_space_queue[i]]
if current_chunk:
    free_chunks.append(current_chunk)

min_free_space = min(free_space_queue)

mem_i = -1
while free_space_queue:

    while memory[mem_i] == "." or moved[len(memory)+mem_i]: 
        mem_i -= 1
    

    if min_free_space >= len(memory)+mem_i:
        break
    chunk = []
    chunk_is = []
    chunk.append(memory[mem_i])
    chunk_is.append(mem_i)
    mem_i -= 1

    while memory[mem_i] == chunk[0]:
        chunk.append(memory[mem_i])
        chunk_is.append(mem_i)
        mem_i -= 1
    
    for i in range(len(free_chunks)):
        if len(free_chunks[i]) >= len(chunk) and free_chunks[i][0] < (chunk_is[0] + len(memory)):
            while chunk_is:
                ind = free_chunks[i].pop(0)
                chunk_i = chunk_is.pop()
                memory[ind] = chunk[0]
                memory[chunk_i] = "."
            break


checksum = 0
for id in range(0, len(memory)):
    if memory[id] != ".":
        checksum += id*int(memory[id])

print(f"p1: {checksum}")