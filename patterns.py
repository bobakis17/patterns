figure = input()

if figure == 'rectangular triangle':
    rows = int(input())
    stars = 1

    for r in range(rows):
        for symbols in range(stars):
            print('*', end='')

        print("")
        stars += 1
elif figure == 'square':
    row_line = int(input())
    for i in range(row_line):
        if i == 0 or i == row_line - 1:
            for l in range(row_line):
                print('*', end='')

            print('')

        else:
            print('*' + (row_line - 2) * " " + '*')
elif figure == 'pyramid':
    pass
elif figure == 'diamond':
    pass
