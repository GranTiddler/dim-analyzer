from math import *


class MathList:
    def __init__(self):
        self.data = []

    def set_data(self, data):
        self.data = data

    def listwise(self, num):
        e = []
        for i in self.data:
            e.append(num.stink(i))
        return e


class Lambda:
    def __init__(self):
        fx = input("Enter a function using the variable \"x\": ")
        self.greg = eval(f"lambda x: {fx}")

    def stink(self, input):
        return self.greg(input)


def split_parentheses(strang):
    output = []
    last = 0
    last_closed = -1
    layers = 0
    current = 0
    opened = False

    complete = True

    for i in range(len(strang)):
        for j in range(len(strang[i])):
            if strang[i][j] == "(":

                complete = False

                if layers == 0:
                    last = current

                    temp = strang[i][last_closed + 1:j]
                    if temp and ")" not in temp:
                        output.append(temp)

                    current = j
                    opened = True

                layers += 1

            elif strang[i][j] == ")" and opened:
                if layers == 1:
                    opened = False

                    output.append([strang[i][current + 1:j]])
                    last_closed = j
                layers -= 1

        if last_closed != j:
            output.append(strang[i][last_closed + 1:])
        if last_closed == -1:
            return strang

    if not complete:
        for i in range(len(output)):
            if "(" in output[i][0]:
                output[i] = (split_parentheses(output[i]))

    return output


def format_string(stringo):
    temp = ""
    for i in stringo:
        if i != " ":
            temp += i
    return temp


def divide_units(listoid, above = True, layers = 0):
    top = []
    bottom = []
    layers += 1
    if type(listoid) == list and listoid:
        for i in listoid:
            temp = divide_units(i, above)
            top += temp[0]
            bottom += temp[1]
            above = temp[2]

    elif type(listoid) == str:
        for i in listoid:
            if i == "/":
                above = not above
            elif above:
                top.append(i)
            else:
                bottom.append(i)

    return [top, bottom, above]


def pow_units(strang):
    previous = 0
    temp = ""

    for i in range(len(strang)):
        if i + 2 < len(strang) and strang[i:i+2] == "**":
            temp += strang[previous:i-1] + strang[i-1] * int(strang[i+2])
            previous = i

    return temp


def get_units(inp):
    inp = format_string(inp)
    inp = pow_units(inp)


thing = input("eee: ")

carl = pow_units(thing)
print(carl)