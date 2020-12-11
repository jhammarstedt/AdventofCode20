import sys

def task1(data):
    data.sort() 
    charging = 0
    one = 0
    three= 0

    if data[0] ==1: 
        one+=1
    else: 
        three +=1
    for i,val in enumerate(data[:len(data)-1]):
        diff = data[i+1]-val 
        if  diff== 1:
            one+=1
        else:
            three+=1

    built_in = data[-1]+3
    three+=1
    print('final threes',three)
    print('final ones',one)
    print(three*one)

def task2(lines):
    # Part 2 - Not my own solution: https://dev.to/qviper/advent-of-code-2020-python-solution-day-10-30kd
    sol = {0:1}
    for line in sorted(lines):
        sol[line] = 0
        if line - 1 in sol:
            sol[line]+=sol[line-1]
        if line - 2 in sol:
            sol[line]+=sol[line-2]
        if line - 3 in sol:
            sol[line]+=sol[line-3]

    print(sol[max(lines)])



def main():
    data = []
    for input in sys.stdin:
        data.append(int(input.strip()))
    task1(data)
    task2(data)

if __name__ == "__main__":
    main()
