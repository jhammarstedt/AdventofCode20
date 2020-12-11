import sys
from collections import deque
import numpy as np


def valid(nrs:deque,tal:int)->bool:
    """checks if there is a sum of two numbers that adds up to tal"""
    nrs = sorted(nrs)
    nrs = deque(nrs)
    if isinstance(nrs,list):
                raise TypeError('Input is list')
    while len(nrs)>=1:
        summa = nrs[0]+nrs[-1]
        if summa==tal:
            return True #correct
        elif summa < tal: #we need to increase the sum, remove smallest element
            nrs.popleft()
        else: #need to make it smaller
            nrs.pop()
    return False

def invalid_nr(data:list)->int:
    nbrs = deque(data[0:25])
    for i,nr in enumerate(data[25:]): #start with the 26th nbr
        if not valid(nbrs,nr):
            return nr
        else:
            nbrs.popleft() #remove previous
            nbrs.append(nr) #add next
    raise Exception('Out of loop, something is wrong')

def task2(inv:int,data:list):
    """Sort a new list of numbers, brute force solution"""
    startI = 0
    endI= 2
    


    while endI < len(data):
        summa = sum(data[startI:endI])
        if summa == inv:
            final = sorted(data[startI:endI])
            return (final[0]+final[-1])
        if summa < inv:
            endI +=1
        else:
            startI+=1
        
def main():
    data=[]
    for input in sys.stdin:
        data.append(int(input.strip()))
    inv = invalid_nr(data)
    print(inv)
    print('key',task2(data=data,inv=inv))
#
if __name__ == "__main__":
    main()            