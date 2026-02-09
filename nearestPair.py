list1 = [1, 45, 99, 108, 89, 95, 98]

diff_dict = {}

for i in range(0, len(list1)):
    for j in range(i + 1, len(list1)):
        diff = abs(list1[i] - list1[j])
        diff_dict[diff] = (list1[i], list1[j])

# extract and sort the differences
list2 = list(diff_dict.keys())
list2.sort()

# smallest difference is at index 0
min_diff = list2[0]

# fetch the nearest pair
nearest_pair = diff_dict[min_diff]

print(nearest_pair)
