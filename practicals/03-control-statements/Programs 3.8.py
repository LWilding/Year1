if __name__ == '__main__':

    while True:
        x = int(input('Enter a number between 0-12: '))
        if -12 <= x <= -1:
            y = -x
            for n in reversed(range(0, 13)):
                print(n, 'x', y, '=', y * n)

        if 0 <= x <= 12:
            for n in range(0, 13):
                print(n, 'x', x, '=', x * n)
        break
