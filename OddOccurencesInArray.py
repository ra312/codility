# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#  0.040 s
# RUNTIME ERROR, tested program terminated with exit code 1
# stderr:

# Traceback (most recent call last):
#   File "exec.py", line 129, in <module>
#     main()
#   File "exec.py", line 91, in main
#     result = solution( A )
#   File "/tmp/solution.py", line 12, in solution
#     return [num for num, counted in hashmap.items() if counted==1].pop()
# IndexError: pop from empty list


#  stderr:

# Traceback (most recent call last):
#   File "exec.py", line 129, in <module>
#     main()
#   File "exec.py", line 91, in main
#     result = solution( A )
#   File "/tmp/solution.py", line 12, in solution
#     return [num for num, counted in hashmap.items() if counted==1].pop()
# IndexError: pop from empty list



# stderr:

# Traceback (most recent call last):
#   File "exec.py", line 129, in <module>
#     main()
#   File "exec.py", line 91, in main
#     result = solution( A )
#   File "/tmp/solution.py", line 12, in solution
#     return [num for num, counted in hashmap.items() if counted==1].pop()
# IndexError: pop from empty list




    
def solution(A):
    # write your code in Python 3.6
    # print(A)
    hashmap = {num:0 for num in A}
    # print(hashmap)
    for num in A:
        hashmap[num] += 1
    
    return [num for num, counted in hashmap.items() if counted==1].pop()

    
    
