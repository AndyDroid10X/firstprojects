arena = []
bonuses = []
voids = []
walls = []
h, w = map(int, input().split(" "))
x = 0
y = 0
for i in range(h):
    arena.append(list(input()))

for i in arena:
    for j in i:
        if 'B' == j:
            bonuses.append([x, y])
        y+=1
    x+=1
    y=0
x=0
for i in arena:
    for j in i:
        if '.' == j:
            voids.append([x, y])
        y+=1
    x+=1
    y=0
x=0
for i in arena:
    for j in i:
        if 'W' == j:
            walls.append([x, y])
        y+=1
    x+=1
    y=0


bcount = 0
brecord = 0
for i in voids:
    if bonuses == [] and walls == []: break
    for j in range(h//2):
        j+=1
        if "W" in  arena[i[0]-j][i[0]]:
            break
        elif "B" in  arena[i[0]-j][i[0]]:
            bcount+=1
    for j in range(h//2):
        j+=1
        if "W" in  arena[i[0]+j][i[0]]:
            break
        elif "B" in  arena[i[0]+j][i[0]]:
            bcount+=1
    for j in range(w//2):
        j+=1
        if "W" in  arena[i[0]][i[1]+j]:
            break
        elif "B" in  arena[i[0]][i[1]+j]:
            bcount+=1
    for j in range(w//2):
        j+=1
        if "W" in  arena[i[0]][i[1]-j]:
            break
        elif "B" in  arena[i[0]][i[1]-j]:
            bcount+=1
    if bcount > brecord:
        brecord = bcount
        out = i
    bcount = 0
if brecord == 0: print("1 1")
else:
    out[0], out[1] = out[0]+1, out[1]+1
    print(' '.join(map(str, out)))
