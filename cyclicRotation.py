# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    n = len(A)

    if n == 0:
        return A
        
    if K == 0 or K == n:
        return A
    
    if K > n:
        K = K % n
    
    for _ in range(K):
        # if A is empty or short, i.e. len(A)<K
        right = A.pop()
        A.insert(0, right)
        
    return A

