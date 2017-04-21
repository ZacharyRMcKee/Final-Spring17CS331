import sys

def file_to_dict(file):
    chars = [0]*128
    with open(file) as f:
        content = f.readlines()
    for line in content:    
        for c in line:
            index = ord(c)
            if index < 128:
                chars[index] += 1
            else:
                print("File has non-ASCII (dec < 128) characters. Please use ASCII-encoded text files only.")
                print("Enter any character to continue (ignoring the non-ASCII character) or 'exit' to quit.")
                dummy = input()
                if input == "exit" or input == "'exit'":
                    sys.exit()
    print("Frequency of characters -- format: CHAR -- FREQ")
    for i in range(128):
        print(repr(chr(i)) + " -- " + str(chars[i]))
    print()
    out = {chr(x): chars[x] for x in range(128)}
    return out

