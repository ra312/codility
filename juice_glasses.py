# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(juice, capacity):
    # write your code in Python 3.6
    n = len(juice)
    maximum_number_of_flavours = n
    if n==2:
        if sum(juice)> max(capacity):
            return 1
    

    free_space = [c - j for c, j in zip(capacity,juice)]

    max_free_space = max(free_space)
    glass_with_max_space = free_space.index(max_free_space)
    juice=sorted(juice, reverse=False)
    capacity=sorted(capacity, reverse=False)


    juice.remove(glasses_to_be_used)

    if sum(juice) <= max_free_space:
        return maximum_number_of_flavours
    else:
        juice.pop()


    
    


    
    return 1
# k = 0, 1, 2, ..., N-1 glasses with at least one unit J of juice
# juice[k] is the flavour and capacity[k] is the capacity of the glass

# flavour = number of different glasses mixed together
# if we put k glasses into one fixed glass, then the flavour=k+1
# number of ways 
