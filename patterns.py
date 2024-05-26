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
    pass
elif figure == 'pyramid':
    pass
elif figure == 'diamond':
    pass
