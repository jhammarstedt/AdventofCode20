import sys

def count(g:list)->int:
    return len(set(''.join(g))) #count the unique values in the group
def task1(data:list):
    group = []
    yes = 0
    for ind,i in enumerate(data):
        if i =='':
            yes += count(group)# getting the numbers of unique letters in each group which is the amount of yes   
            group = []
        else:
            group.append(i)
            if ind == len(data)-1: #last one
                yes+= count(group)
        
    print(yes)
def task2(data:list):
    yes =0
    group =[]
    for ind,i in enumerate(data):
        if i =='':
            yes += len(set.intersection(*group))
            group = []
        else:
            group.append(set(i))
            if ind == len(data)-1: #last one
                yes += len(set.intersection(*group))     
    print(yes)
def main():
    data = []
    for input in sys.stdin:
        data.append(input.strip())
    
    task1(data)
    task2(data)
    
if __name__ == "__main__":
    main()