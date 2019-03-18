'''Program Parses specific columns from CSV data then graphs it.'''
import pylab


def parse_token(token, str_pos_lst, token_pos):
    '''Returns str for tokens in str_pos_list; Returns floats for all others'''
    if token_pos in str_pos_lst:
        return str(token)
    else:
        return float(token)


def parse_line(line, string_pos_lst, sep):
    '''Parsed line into tokens and converst them to str() or float()'''
    return [parse_token(token, string_pos_lst, token_pos)
            for token_pos, token in enumerate(line.rstrip('\n').split(sep))]


def get_csv_data(f_obj, string_pos_lst, sep=","):
    '''Returns a nested list called data_lst'''
    if sep != ',':
        print("invalid separator: file is comma separated")
        return []

    data_lst = []
    header_row = f_obj.readline()
    data_lst.append(header_row.rstrip('\n').split(sep))
    print(data_lst)
    for data_row in f_obj:
        try:
            data_lst.append(parse_line(data_row, string_pos_lst, sep))
        except ValueError:
            continue
    for row in data_lst:
        print(row)
    return data_lst


def print_data(data):
    '''Prints data in lines'''
    for line in data:
        print(line)


def get_index(row, heading):
    '''Returns index of the desired column within the given row'''
    return row.index(heading)


def fill_col(data_lst, col):
    return [row[col] for row in data_lst]


def get_columns(data_lst, cols_lst):
    '''Returns column data for each heading given in columns list'''
    if cols_lst == []:
        return []
    col_positions = []
    for col in cols_lst:
        if col in data_lst[0]:
            col_positions.append(get_index(data_lst[0], col))
        else:
            continue
    return [fill_col(data_lst, col) for col in col_positions]

    # col_pos_lst = [get_index(data_lst[0], col_name) for col_name in cols_lst]
    # return [fill_col(data_lst, col) for col in col_pos_lst]


def main():
    '''Main Function'''
    bb_file = open("lb-james.csv", "r")
    bb_lst = get_csv_data(bb_file, [0, 2, 3, 4], ",")
    columns = get_columns(bb_lst, ['3P%', '2P%', 'FT%'])
    for row in columns:
        print(row)

    x = [i for i in range(4, len(columns[0])+3)]
    y_3fg = [columns[0][i] for i in range(1, len(columns[0]))]
    y_2fg = [columns[1][i] for i in range(1, len(columns[1]))]
    y_ft = [columns[2][i] for i in range(1, len(columns[2]))]
    xy1 = zip(x, y_2fg)
    xy2 = zip(x, y_3fg)
    xy3 = zip(x, y_ft)
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []

    for x, y in xy1:
        x1.append(x)
        y1.append(y)
    for x, y in xy2:
        x2.append(x)
        y2.append(y)
    for x, y in xy3:
        x3.append(x)
        y3.append(y)

    pylab.title('Lebrons FG percentage')
    fg2, = pylab.plot(x1, y1, color='blue', label='2FG')
    fg3, = pylab.plot(x2, y2, color='red', label='3FG')
    fth, = pylab.plot(x3, y3, color='green', label='FT')
    pylab.legend(handles=[fg2, fg3, fth])
    pylab.xlim(1, 15)
    pylab.ylim(0, 1)
    pylab.show()


if __name__ == '__main__':
    main()
