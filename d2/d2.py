import sys
data = []
for input in sys.stdin:
        data.append(input.strip())

b = [i.split(' ') for i in data]
b = [[i[0].split('-'),i[1][:-1],i[2]] for i in b]

def problem1(b=b,valid=0):
    for i in b:
        lower = int(i[0][0])
        upper = int(i[0][1])
        letter = i[1]
        c = i[2].count(letter)
        if (c>=lower) and (c<=upper):
            valid +=1
    return valid

def problem2(b=b,valid=0):
    for i in b:
        index1 = int(i[0][0])-1 #since we have no 0
        index2 = int(i[0][1])-1
        letter = i[1]

        if (i[2][index1] == letter) or (i[2][index2]==letter):
            if (i[2][index1] != i[2][index2]):          
                valid +=1
    return valid

ans1 = problem1()
ans2 = problem2()
print(ans1,ans2)
