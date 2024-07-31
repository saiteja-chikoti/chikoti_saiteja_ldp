n = 6
a = [1, 2, 3, 4, 5, 6]

mov = (n // 2) + (n % 2)
now = mov

even = sum(1 for x in a if x % 2 == 0)
odd = n - even

while True:
    if now < 0:
        print("Bob")
        break

    val1 = now + now - 1
    val2 = mov - now + mov - now

    if even >= val1 and odd >= val2:
        print("Alice")
        break

    val1 = now + now
    val2 = mov - now + mov - now - 1

    if even >= val1 and odd >= val2:
        print("Alice")
        break

    now -= 2


