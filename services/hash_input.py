import sys

def file_to_dict(content):
    chars = [0]*128

    i = 0
    for line in content:
        i += 1
        if i % 1000 == 0:
            print("Scanning line " + str(i),end=" ... \r")
        
        for c in line:
            index = ord(c)
            #if index < 128:
            chars[index] += 1
            #else:
            #    print("File has non-ASCII (dec < 128) characters. Please use ASCII-encoded text files only.")
            #    print("Enter any character to continue (ignoring the non-ASCII character) or 'exit' to quit.")
            #    dummy = input()
            #    if input == "exit" or input == "'exit'":
            #        sys.exit()
    print("Scanning finished.")
    print("Frequency of characters -- format: CHAR -- FREQ")
    for i in range(128):
        print(repr(chr(i)) + " -- " + str(chars[i]))
    print()
    out = {chr(x): chars[x] for x in range(128)}
    return out

