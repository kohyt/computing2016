try:
    
    # open file
    infile = open("CURRENCIES.TXT",'r')
    file = open("UPDATED.TXT",'r')

    # read file
    lines = infile.readlines()
    file_lines = file.readlines()

    # close file
    infile.close()
    file.close()

    for line in range(len(lines)):
        lines[line] = lines[line].strip().split(",")

    for line in range(len(file_lines)):
        file_lines[line] = file_lines[line].strip().split(",")

    print(lines)
    print()
    print(file_lines)
    print()

    # check for similar countries in updated files with the original
    # update the respective currencies
    # for the countries in updated but not in currencies,
    # add into the file
    # write all the updated information into newcurriencies.txt

    # hashing function
    def HashKey(country):
        asc = 0
        for x in range(len(country)):
            # calculate ascii code for each character within name
            # and add total ascii values
            asc += ord(country[x])
            
            # divide by prime number and modulo to get remainder
            remainder = (asc % 33)

            # +1 is the address for the record
            address = remainder + 1
            return address


    print(HashKey("argentina"))
        
except FileNotFoundError:
    print("CURRENCIES.TXT not found.")
