try:

    # open file
    infile = open("MARKS.TXT",'r')

    # read file
    lines = infile.readlines()

    # close file
    infile.close()

    for line in range(len(lines)):
        lines[line] = lines[line].strip().split(",")

    highest = 0
    student = []
    total = 0

    # iterate through the data in file to get highest mark
    for x in range(len(lines)):
        lines[x][2] = int(lines[x][2])
        if lines[x][2] > highest:
            highest = lines[x][2]

        # summing up all the marks to find average 
        total += lines[x][2]

    # iterate through data to find students with the highest mark
    # may have more than 1 student scoring the highest mark
    for x in range(len(lines)):
        if lines[x][2] == highest:
            student.append(lines[x][1])

    # output highest mark and student(s) who achieved it
    for i in range(len(student)):
        print("Highest mark {} achieved by {}".format(highest,student[i]))

    # output average mark of module, rounded to 2d.p
    average = total / len(lines)
    print("The average mark of the module is {:.2f}.".format(average))

    for x in range(len(lines)):
        if lines[x][2] == 95:
            lines[x].append("M")
        elif lines[x][2] < (average - 10):
            lines[x].append("F")
        else:
            lines[x].append("P")

    print(lines)

    # open file
    file = open("GRADES.TXT",'w')

    # write file
    for x in range(len(lines)):
        file.write(lines[x][0] + "," + lines[x][1] + "," + str(lines[x][2]) + "," + "{:.2f}".format(average) + "," + lines[x][3] + "\n")

    # close file
    file.close()
        

except FileNotFoundError:
    print("MARKS.TXT not found.")
