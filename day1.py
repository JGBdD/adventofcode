from utils import get_input

data = get_input(day=1).splitlines()
increases = 0
depths = [int(d) for d in data]

for i in range(1 , len(depths)-3):
    previous = depths[i-1 : i+2]
    depth = depths[i : i+3]

    if i < 1990: print(previous , depth)

    if sum(depth) > sum(previous):
        increases += 1


print(increases)