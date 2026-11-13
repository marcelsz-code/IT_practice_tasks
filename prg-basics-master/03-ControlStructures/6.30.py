for start in range(1, 8):
    row = [str(num) for num in range(start, 50, 7)] #zwiększa każdą kolejną wartość o 7
    print(" ".join(row))
