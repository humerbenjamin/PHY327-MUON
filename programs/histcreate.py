import matplotlib.pyplot as plt

def read_histfile(filename):
    f = open(filename, "r")
    lines = f.readlines()
    return make_arr_fromlines(lines)


def make_arr_fromlines(lines):
    newlines = []
    for i in range(len(lines)):
        newlines.append([])
        valnum = 0
        newlines[i].append("")
        for letter in lines[i]:
            if letter == " ":
                newlines[i][valnum] = float(newlines[i][valnum])
                valnum += 1
                newlines[i].append("")
            elif letter == "\n":
                newlines[i][valnum] = float(newlines[i][valnum])
                exit
            else:
                newlines[i][valnum] = newlines[i][valnum] + (letter)

    return newlines


def give_columns(lines, columns):
    cols = []
    for colnumber in columns:
        cols.append(give_column(lines, colnumber))

    return cols[0], cols[1], cols[2]

def give_column(lines, colnumber):
    column = []
    if colnumber == 1:
        for i in range(len(lines)):
            column.append(lines[i][0])
    elif colnumber == 2:
        for i in range(len(lines)):
            column.append(lines[i][1])
    elif colnumber == 3:
        for i in range(len(lines)):
            column.append(lines[i][2])
    else:
        print("INVALID COLNUMBER")
    return column

            
def makeplot_hist(filename):
    lines = read_histfile(filename)
    col1, col2, col3 = give_columns(lines, [1, 2, 3])

    # graph hist
    plt.bar(col1, col3)
    plt.show()



if __name__ == '__main__':
    filename = "hist_27-09-22_liq_1h_2.txt"
    makeplot_hist(filename)