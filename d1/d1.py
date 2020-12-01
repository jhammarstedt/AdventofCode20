# Find the 3 unique numbers that sum to 2020
import sys
data = []
for input in sys.stdin:
        data.append(int(input.strip()))

data.sort()
aind = 0
bind = 1
cind = len(data)-1
a=b=c= 0 #random starting values

while a+b+c != 2020:  
    a = data[aind] 
    b = data[bind]
    c = data[cind]
    if a+b+c == 2020: #done
        print(a,b,c)
        print(a*b*c)
        break
    elif a+b+c>2020: #too big so shift c down
        cind -=1
    elif cind <= bind: #reset
        aind +=1
        bind = aind+1
        cind = len(data)-1
    else:              # sum is too small so we increase b
        bind +=1
        