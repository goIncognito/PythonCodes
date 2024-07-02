dict1 = {1: "Anubhav", 2: "Anish", 3: "Jungle Book", 4: "Bangalore"}


def reversed_dict(original_dict):
    reversed_items = list(original_dict.items())[::-1]
    reverse_dict = dict(reversed_items)
    return reverse_dict


reverse_dict = reversed_dict(dict1)
print("Original Dict:", dict1)
print("Reversed Dict: ", reverse_dict)
