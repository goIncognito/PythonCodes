input_str = "Aapplee are ggreatt souurcce of vittaminss"

seen = set()      # to track letters we've already added
result = []       # to build the final string

for char in input_str:
    if char == " ":          # always keep spaces
        result.append(char)
    elif char not in seen:   # only add letters we haven't seen
        seen.add(char)
        result.append(char)

output_str = "".join(result)
print(output_str)
