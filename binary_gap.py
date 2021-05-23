# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    
    binary_string = str(bin(N)[2:])
    if binary_string.rfind('1')==0:
        # i.e., N = 1000000...0000
        # and there is no binary gap
        return 0
    in_binary_zeroes = True
    longest_gap = 0
    counted_binary_zeroes = 0
    print(binary_string)
    for char in binary_string:
        if char == '1':
            if longest_gap < counted_binary_zeroes:
                longest_gap = counted_binary_zeroes
            in_binary_zeroes = False
            counted_binary_zeroes = 0
        else:
            in_binary_zeroes==True
            counted_binary_zeroes += 1
    return longest_gap



if __name__ == '__main__':
    tests = [
        dict(N=1041),
        dict(N=15),
        dict(N=32)
    ]

    for test in tests:
        answer  = solution(**test)
        print(test, answer)



