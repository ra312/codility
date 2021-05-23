# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # print(A)
    hashmap = {num:0 for num in A}
    # print(hashmap)
    for num in A:
        hashmap[num] += 1
    
    return [num for num, counted in hashmap.items() if counted==1].pop()

    
    
