#include <iostream>
#include <algorithms>
from typing import List

def solution(A: List[int], L:int, R:int)-> int:
    ans = 0
    sorted(A, reverse=False)
    # sort(A.begin(), A.end());


    for k in range(0,len(A),1):
        if A[k]> R:
            ans += 1
            R = A[k]
            A[k]=0
    
    for k in range(len(A)-1,-1,-1):
        if A[k] < L:
            ans += 1
            L = A[k]
            A[k]=0
    return ans


if __name__ == '__main__':
    test_input_values = [
        #  ([2, 3, 3, 4], 3, 1)
        #  ,([5, 2, 5, 2], 8, 1)
        #  ,([1, 5, 5], 2, 4)
        ([2,3,3,4],3,1)
        #  ([1,2],2,1)
        #  ,([2,1],2,1)
        #  ,([3,7],2,8)
        #  ,([7,4,9],100,100)
        #  ,([1,2,3,4],3,5)

    ]
    test_outputs = [
        #  4
        #  ,4
        #  ,2
        3
        #  2
        #  ,2
        #  ,0
        #  ,3
        #  ,2
    ]
    
    test_inputs = [dict(A=v[0], L=v[1], R=v[2]) for v in test_input_values]
    num_of_tests=len(test_inputs)
    counted = 0
    test_hashmap = {k:True for k in range(num_of_tests)}
    for k, input_output in enumerate(zip(test_inputs, test_outputs)):
        input, output = input_output
        real_output = solution(**input)
        
        if real_output != output:
            test_hashmap[k]=False
            counted += 1
            print(f"{input}->{real_output}!={output}")
    if counted > 0:
        print(f"There are {counted} out of {num_of_tests} failed tests!")
        # for k in test_hashmap.keys():
        #     if test_hashmap[k] is True:
        #         input = test_inputs[k]
        #         output = solution(**input)
        #         expected_output = test_outputs[k]
        #         print(f"{input}->{output}!={expected_output}")
    else:
        print("All tests passed!")