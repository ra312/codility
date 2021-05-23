# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    
    
    binary_string = bin(N)[2:]
    if binary_string.rfind('1')==0:
        # i.e., N = 1000000...0000
        # and there is no binary gap
        return 0
    return max([ len(zeroes) for zeroes in bin(N)[2:].split('1')])
