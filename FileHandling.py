
with open("SampleTextFile.txt" , "a+") as f:
    new_line = "\nI am learning DSA now\n"
    f.write(new_line)
    f.seek(0)
    lines = f.readlines()[-1]
    print(lines)
