i = 6
while i >= 0:
    j = 1 #j jest resetowane przy każdym nowym wierszu
    while j < 4:
        print(f'{i+j}', end=' ')
        j += 1 #ręczna zmiana wartości liczników
    print()
    i -= 3 #ręczna zmiana wartości liczników
