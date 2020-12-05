import sys

def find_seat(code:str) -> int:
    upper =127
    lower = 0
    col_l = 0
    col_u = 7
    for i in code: 
        if i =='F':
            diff = upper- lower
            upper = upper - (int(diff/2) +diff%2)
        if i =='B':
            diff = upper-lower
            lower = lower + int(diff/2) + diff%2
        if i =='L':
            diff = col_u- col_l
            col_u = col_u - (int(diff/2) +diff%2)
        if i =='R':
            diff = col_u - col_l
            col_l = col_l + int(diff/2) + diff%2
    #print('Seat',upper,col_u)
    return (upper*8)+col_u
def main():
    max_id = 0
    ids = []
    for input in sys.stdin:
        code = input.strip()
        new_id = find_seat(code)
        ids.append(new_id)
        max_id = max(new_id,max_id)
    
    ids.sort()
    for index,id in enumerate(ids):
        if index+ids[0] != id:
            missing = index+ids[0]
            break
    print('Max id on plane: ',max_id)
    print('Your missing ID:', missing)





if __name__ == "__main__":
    main()