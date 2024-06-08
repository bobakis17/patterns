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
    rows = int(input())
    space_counter = (rows - 1) // 2

    for i in range(rows):
        if i % 2 != 0:
            continue
        else:
            if i != rows - 1:
                print(space_counter * ' ', end='')
            for stars in range(i + 1):
                print('*', end='')

            print('')

            space_counter -= 1
elif figure == 'diamond':
    rows = int(input())
    space_counter = (rows - 1) // 2

    for i in range(rows):
        if i % 2 != 0:
            continue
        else:
            if i != rows - 1:
                print(space_counter * ' ', end='')
            for stars in range(i + 1):
                print('*', end='')

            print('')

            if i == rows - 1:
                continue

            space_counter -= 1

    for index in range(rows - 2, -1, -1):
        if index % 2 != 0:
            continue
        else:
            space_counter += 1

            print(space_counter * ' ', end='')

            for stars in range(index + 1):
                print('*', end='')

            print('')