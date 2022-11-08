# Example Code!
# Merge Sorting:

def merge(a,b):
    merged_list = []
    len_a,len_b = len(a),len(b)
    index_a,index_b = 0,0

    while index_a < len_a and index_b < len_b:
        if a[index_a] < b[index_b]:
            merged_list.append(a[index_a])
            index_a += 1
        else:
            merged_list.append(b[index_b])
            index_b += 1

    if index_a < len_a:
        merged_list.extend(a[index_a:])
    elif index_b < len_b:
        merged_list.extend(b[index_b:])
    return merged_list

# Now merge sorting:
def merge_sort(L):
    if len(L) <= 1:
        return L
    mid = len(L)//2
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    return merge(left,right)

# input list:
L = [[4,7,2,3],[10],[10,9,8,7,6],[2,3,1],[1,2],[2,1]]
total_sorted_list = []
for i in L:
    sorted_list = merge_sort(i)
    print("Original List:",i)
    print("Sorted List:",sorted_list)
    print()