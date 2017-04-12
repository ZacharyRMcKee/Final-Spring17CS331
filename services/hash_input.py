import sys

def file_to_dict(file):
    chars = {chr(x): 0 for x in range(128)}
    with open(file) as f:
        content = f.readlines()
    lineno = 0
    charno = 0
    for line in content:
        charno = 0
        lineno += 1
        for c in line:
            charno += 1
            if ord(c) < 128:
                chars[c] += 1
            else:
                print("File has non-ASCII (dec < 128) characters. Please use ASCII-encoded text files only.")
                print(ord(c))
                print("Found at line " + str(lineno) + ", char " + str(charno))
                print("Enter any character to continue (ignoring the non-ASCII character) or 'exit' to quit.")
                dummy = input()
                if input == "exit" or input == "'exit'":
                    sys.exit()
    print("Frequency of characters -- format: CHAR -- FREQ")
    for i in chars:
        print(repr(i) + " -- " + str(chars[i]))
    print()
    return chars 