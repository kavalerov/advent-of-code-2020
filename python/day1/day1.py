with open("input.txt", "r") as ifile:
    lines = ifile.readlines()
    for startIndex, item in enumerate(lines):
        for secondItem in lines[startIndex:]:
#            print("First: " + str(item))
#            print("Second: " + str(secondItem))
#            print("Sum: " + str(item + secondItem))
            if (int(item) + int(secondItem)) == 2020:
                print(int(item) * int(secondItem))