"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    if x<=1:
        return x
    else:
        return foo(x-1)+foo(x-2)

def longest_run(mylist, key):
    ### TODO
    if not mylist:
        return Result(0, 0, 0, False)

    longest_size = 1
    current_run = 0
    left_size = 0
    right_size = 0
    is_entire_range = True 

    for i in mylist:
        if i == key:
            left_size += 1
        else:
            break

    for i in reversed(mylist):
        if i == key:
            right_size += 1
        else:
            break

    for i in mylist:
        if i == key:
            current_run += 1
            if current_run > longest_size:
                longest_size = current_run
            current_run = 0

    if current_run > longest_size:
        longest_size = current_run

    if left_size + right_size + longest_size == len(mylist) and longest_size > 1:
        is_entire_range = True
    else:
        is_entire_range = False 

    return Result(longest_size, left_size, right_size, is_entire_range)


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    ### TODO
    if not mylist:
        return Result(0, 0, 0, False)

    def helper(sublist, current_run, max_run):
        if not sublist:
            return max_run

        if sublist[0] == key:
            current_run += 1
        else:
            max_run = max(max_run, current_run)
            current_run = 0

        return helper(sublist[1:], current_run, max_run)

    max_run = helper(mylist, 0, 0)
    return Result(max_run, 0, 0, True)



