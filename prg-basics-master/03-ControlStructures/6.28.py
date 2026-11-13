a= 0
b = 1
for _ in range(20): #_ zmienna nie używana
    print(a, end=" ")
    a, b = b, a + b
