#import pdb

def get_total(lst):
    index = 0
    total = 0
    #pdb.set_trace()  # breakpoint
    while index < len(lst):
        total += lst[index]
        index += 1

    print(total)
    #pdb.set_trace()  # breakpoint
    return total
print(get_total([2, 4, 6, 8]))
