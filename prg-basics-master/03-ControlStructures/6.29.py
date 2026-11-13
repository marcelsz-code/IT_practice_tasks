n = int(input("Podaj liczbę N: "))
count = 0  # licznik znalezionych liczb pierwszych
candidate = 2  # aktualnie sprawdzana liczba; od 2
primes = []  # lista przechowująca znalezione liczby pierwsze

while count < n:
    is_prime = True

    for divisor in range(2, candidate):# sprawdzenie, czy candidate dzieli się przez jakąkolwiek liczbę od 2 do candidate - 1
        if candidate % divisor == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(str(candidate))
        count += 1

    candidate += 1

print("Prime numbers:", " ".join(primes))
