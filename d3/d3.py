import sys
data = []
for input in sys.stdin:
        data.append(input.strip())


strats = [[1,1],[1,3],[1,5],[1,7],[2,1]]
all_t = []
prods=1
for i in strats:
    col = 0
    row = 0
    trees = 0
    while row < len(data):
        if data[row][col]=='#': #hit a tree
            trees+=1    
        col = (col + i[1])%len(data[0])
        row +=i[0]
    print(trees)
    prods *= trees
    all_t.append(trees)
print(prods)