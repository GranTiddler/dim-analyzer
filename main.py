from math import *

import imath


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

    def stink(self, inp):
        return self.greg(inp)


class Unit:
    def __init__(self, symbol):
        self.symbols = {
            "m": 0,
            "s": 0,
            "kg": 0,
            "hz": 0,
            "n": 0,
            "j": 0,
            "W": 0
        }
        for i in symbol[0]:
            self.symbols[i] += 1

        for i in symbol[1]:
            self.symbols[i] -= 1

    def simplify(self):
        simplified = False

        n_sign = imath.sign(self.symbols["m"])
        if self.symbols["m"] * n_sign >= 1 and self.symbols["kg"] * n_sign >= 1 and self.symbols["s"] * n_sign <= -2:
            print("reer")
            simplified = True
            self.symbols["kg"] -= 1 * n_sign
            self.symbols["m"] -= 1 * n_sign
            self.symbols["s"] += 2 * n_sign
            self.symbols["n"] += 1 * n_sign

        j_sign = imath.sign(self.symbols["m"])
        if self.symbols["n"] * j_sign >= 1 and self.symbols["m"] * j_sign >= 1:
            simplified = True
            self.symbols["j"] += 1 * j_sign
            self.symbols["n"] -= 1 * j_sign
            self.symbols["m"] -= 1 * j_sign

        if simplified:
            self.simplify()


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
            #above = temp[2]

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
    templist = []
    if type(strang) == str:
        for i in range(len(strang)):
            if i + 2 < len(strang) and strang[i:i+2] == "**":
                temp += strang[previous:i-1] + strang[i-1] * int(strang[i+2])
                previous = i
        return temp
    elif type(strang) == list:
        for i in range(len(strang)):
            if strang[i][0:2] == "**":
                print("WEEE")
                for j in range(eval(strang[i][2:])):
                    templist.append(strang[i-1])


"""
powers
___________
loop through indices
if index is list loop through indices
if index of index is string:
 - if power is not first character apply current code
 - if power is first duplicate previous index and remove power symbol (this will prob break with units but I don't care)
    - remove until first other operator
    - evaluate that section and multiply the thingey by that
    
divide

remove all numeric characters

format the output as unit class? 
"""


def remove_nums(lest):
    temp = ""
    templist =[]
    if type(lest) == str:
        for i in lest:
            if str(i).isdigit() or i == ".":
                pass
            else:
                temp += i
        return temp
    elif type(lest) == list:
        for i in lest:
            templist.append(remove_nums(i))
        return templist


def get_units(inp):
    # remove spaces
    inp = split_parentheses([inp])  # P
    inp = pow_units(inp)            # E
    inp = remove_nums(inp)
    print(inp)

                                    # M is implied
    inp = divide_units(inp)         # D
                                    # A + S don't play in to dimensional analysis
    return inp


thing = input("eee: ")
# carl = get_units(thing)
boy = Unit([["s","s"],["kg", "m", "m"]])
boy.simplify()
print(boy.symbols)
