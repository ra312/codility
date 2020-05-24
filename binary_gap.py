    # you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
	max_len = 0
	zero_length = 0
	detect_gap = 0
	while (N>0):
		if N%2 == 0:
			zero_length +=1
		else: # N%2==1 or N // 2 == 0
			if N // 2 != 0:
				detect_gap += 1
				if zero_length > max_len:
					max_len = zero_length
					zero_length = 0
			else:
				# the trailing zeroes
				print('trailing')
		N = N // 2
    # write your code in Python 3.6
	print(f"detect_gap={detect_gap}")
	if detect_gap <2:
		output = 0
	else:
		output = max_len
	return output
if __name__ == '__main__':
	N = [32,9, 1041, 4]
	failed_these = [6, 19, 1162, 51712, 561892, 74901729, 1376796946]
	for el in failed_these:
		sol = solution(el)
		print(f"{el}->{bin(el)}->{sol}")
