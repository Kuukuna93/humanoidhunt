def getCode(i, row):
    try: 
        #print(i)
        code = row[i: i + 8]
        return int(code, 2)
    except EnvironmentError:
        print("ERROR")

filename = input("Input filename to be parsed:\n")
password = ""

with open(filename, 'r') as fp:
    for i, row in enumerate(fp):
        index = -8
        nextIndex = 9999999999
        nextPassword = ""
        
        #Find first valid code
        while(nextIndex + 8 > len(row)):
            index = index + 8
            nextIndex = getCode(index, row) * 8

        #Find second invalid code
        while(nextIndex + 8 < len(row)):
            nextPassword = getCode(nextIndex, row)
            nextIndex = nextPassword*8
            
        password = password + chr(nextPassword)
        print("Password part " + str(i+1) + ": " + chr(nextPassword) + " - " + str(nextPassword))

print(password)


