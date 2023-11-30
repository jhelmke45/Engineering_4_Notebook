def triangle (set1, set2, set3):    # 3 coordinates as parameters
    try:
        set1 = set1.split(",")      # separate into x and y
        set2 = set2.split(",")
        set3 = set3.split(",")

        x1 = float(set1[0])
        y1 = float(set1[1])
        x2 = float(set2[0])
        y2 = float(set2[1])
        x3 = float(set3[0])
        y3 = float(set3[1])

        area = abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2)    # calculate area

        return area

    except:
        print("invalid input, try again")   # if not correct format, send code to skip print
        area = -1
        return area

while True:
    input1 = input("input coordinate 1: ")
    input2 = input("input coordinate 2: ")
    input3 = input("input coordinate 3: ")

    a = triangle(input1, input2, input3)    # send 3 coordinates to triangle function

    if(a >= 0):
        print(f"area: {a}")     # print area if valid

