def occurance(items):
    char_occurance = {}
    for char in items:
        if char != "":
            if char in char_occurance:
                char_occurance[char] += 1
            else:
                char_occurance[char] = 1
    
    for char, count in char_occurance.items():
        if count > 1:
            print(f"{char} : {count}")

word = input("Enter the string: ")
occurance(word)