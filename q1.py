def decimalToBinary(decimalnumber):
    binary = ""
    
    # convert decimal number to binary
    quotient = decimalnumber
    while quotient > 0:
        remainder = quotient % 2
        quotient = quotient // 2
        
        # string remainder from the back
        binary = str(remainder) + binary
        
    # count the number of "0"s required
    if len(binary) < 8:
        number = 8 - len(binary)
        binary = ("0"*number) + binary

    # return 8-bit binary string result
    return binary

# paste data in decimal.txt 
data = [18,0,255,128,64]

for x in range(len(data)):
    print(decimalToBinary(data[x]))

string = input("Enter 8-bit binary: ")

def bitshift(string):
    # validate input
    allowed = ["0","1"]
    for x in range(len(string)):
        while string[x] not in allowed:
            return False
    
    # range check
    while len(string) < 8 or len(string) > 8:
        print("Not 8-bit binary entered")
        return False

    # presence check
    while len(string) == 0:
        print("No input.")
        return False

    # shift the first bit to the last position
    string = string[1:] + string[0]

    return string
    
print(bitshift(string))

def encryption(plain_text):
    result = ""
    for x in range(len(plain_text)):
        # add 1 to ascii value of each letter in input
        asc = ord(plain_text[x]) + 1

        # convert to 8-bit binary string
        binary = decimalToBinary(asc)

        # shift binary string 1 place to the left
        final = bitshift(binary)

        # concatenate all characters in each string
        result = result + " " + final

    # output 
    return result

for x in range(2):
    plain_text = input("Enter plain text: ")
    print(encryption(plain_text))

    


