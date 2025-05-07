#!/usr/bin/env python3

def print_fibonacci(length):

	our_list = []
	if length > 0:
		our_list.append(0)
	if length >= 2:
		our_list.append(1)
		for _ in range(2, length):
			our_list.append(our_list[-1] + our_list[-2])

	print(our_list)

# Relying on the range:
# def print_fibonacci(length):
    # our_list = []
    # for x in range(length):
    #     if x == 0:
    #         our_list.append(x)
    #     elif x == 1:
    #         new_elem = our_list[x-1] + x
    #         our_list.append(new_elem)
    #     else:
    #         new_elem = our_list[x-1] + our_list[x-2]
    #         our_list.append(new_elem)

    # return our_list


# Test
print(print_fibonacci(9))