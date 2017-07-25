try:

    # open file
    infile = open("WIDEST.TXT",'r')

    # read file
    lines = infile.readlines()

    # close file
    infile.close()

    import datetime

    for line in range(len(lines)):
        lines[line] = lines[line].strip().split(",")

    cities = []
    lowest = []
    highest = []

    # input up to 3 cities with highest and lowest temperatures
    for i in range(3):
        city = input("Enter city: ")
        low = input("Enter lowest temperature: ")
        high = input("Enter highest temperature: ")

        # presence check
        while len(city) == 0 or len(low) == 0 or len(high) == 0:
            print("Please enter value.")
            city = input("Enter city: ")
            low = input("Enter lowest temperature: ")
            high = input("Enter highest temperature: ")

        # data type check
        # city -- alphabets
        while city.isnumeric():
            print("Please enter city name.")
            city = input("Enter city: ")

        # temperatures -- numbers
        while low.isalpha() or high.isalpha():
            print("Please enter integer value.")
            low = input("Enter lowest temperature: ")
            high = input("Enter highest temperature: ")

        # range check
        while int(low) < -90:
            print("Out of range - lowest")
            low = input("Enter lowest temperature: ")

        while int(high) > 60:
            print("Out of range - highest")
            high = input("Enter highest temperature: ")

        # storing values
        cities.append(city)

        # temperatures may have decimals
        lowest.append(float(low))
        highest.append(float(high))

    greatest = 0

    # calculate greatest absolute difference in temperature readings
    for x in range(len(low)+1):
        difference = highest[x] - lowest[x]
        if difference > greatest:
            greatest = difference
            cty = cities[x]
            
    # display city and greatest absolute difference in temperature readings
    print("{} has the greatest absolute difference in temperature readings which is {}".format(cty,greatest))

    # get date of entry
    today = datetime.date.today()

    # convert date as list to string
    current = ""
    for x in range(len(lines[0])):
        current = current + lines[0][x]

    # storing data
    year = int(current[:4])

    if current[5] == 0:
        month = int(current[6])
    month = int(current[5:7])

    day = int(current[8:])

    # convert date as string to date format
    current_date = datetime.date(year,month,day)

    # number of days elapsed since greatest absolute difference
    difference = today - current_date

    # output message for the number of days elapsed
    print("Number of days elapsed since the greatest absolute difference in temperature readings: {}".format(difference.days))

    # comparing if new entry has greater absolute difference
    if greatest > float(lines[1][1]):
    
        # open file
        infile = open("WIDEST.TXT",'w')

        # write file
        infile.write(str(today) + "\n")
        infile.write("{0}".format(cty))
        infile.write("," + str(greatest))

        # close file
        infile.close()


except FileNotFoundError:
    print("WIDEST.TXT not found.")
