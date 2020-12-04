import sys
import re
"""
Not the most efficient approach today, but it allowed me to practice some regex which was good :) 
"""
def read_inp():
    """
    Input parsing, this section needs a lot of improvement given all the list comps and iterations needed now"""
    data = sys.stdin.read()
    data = data.split('\r\n\r\n')
    data = [re.split(' |\r |\r\n',i) for i in data]
    data = [[i.split(':') for i in item] for item in data]
    valid = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])
    sets = [set([i[0] for i in item]) for item in data]
    return data,valid,sets

def task1(data,valid,sets):
    v =0
    for i in sets:
        i.discard('cid')
        if i == valid:
            v+=1 #found a valid id
    print(v)


def check_validity(items: dict):
    """Using regex to check each item, probably not the optimal solution"""
    if not re.match('^(1([0-9][0-9][0-9]))$|(200[0-2])$',items['byr']):
        return False
    elif not re.match('^(201[0-9])$|^(2020)$',items['iyr']):
        return False
    elif not re.match('^(#([0-9]|[a-z]){6})$',items['hcl']):
        return False
    elif not re.match('^(20([1-2][0-9]|30))$',items['eyr']):
        return False
    elif items['ecl'] not in set(['amb','blu','brn','gry','grn','hzl','oth']):
        return False
    elif not re.match('^([0-9]{9})$',items['pid']):
        return False
    elif not re.match('^(1([5-8][0-9]|9[0-3])cm$)|^((([5-6][0-9])|(7[0-6]))in$)',items['hgt']):
        return False
    else: 
        return True
def task2(data,valid,sets):
    """To solve the more specific parsing"""
    data = [{i[0]:i[1] for i in item}for item in data] #convert to dict
    
    v =0 #the actual passports that pass
    for index,items in enumerate(sets):
        items.discard('cid')
        if items == valid: #found a potential valid set
            if check_validity(data[index]):    
                v+=1
    print(v)

def main():
    data,valid,sets = read_inp()
    #task1(data,valid,sets)
    task2(data,valid,sets)
if __name__ == "__main__":
    main()