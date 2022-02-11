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


thing = input("eee: ")
carl = ""
for i in thing:
    if i != "." and i != " ":
        carl +=i


def split_parentheses(strang):
    output = []
    last = 0
    last_closed = 0
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

                    temp = strang[i][last:j]
                    print(temp)
                    if temp and "(" not in temp:
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
        if last_closed == 0:
            return strang

    if not complete:
        for i in range(len(output)):
            if "(" in output[i][0]:
                output[i] = (split_parentheses(output[i]))

    return output


print(split_parentheses([carl]))
