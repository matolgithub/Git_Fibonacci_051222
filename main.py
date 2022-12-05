def fibonacci_1(n=20) -> list:
    fib_list = []
    for item in range(n):
        if item in (0, 1):
            fib_list.append(1)
        else:
            fib_list.append(fib_list[item - 1] + fib_list[item - 2])

    return fib_list  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]


def fibonacci_2(n: int) -> str:
    fib_string = ''
    fib_first, fib_second = 0, 1
    fib_next = fib_first + fib_second
    fib_string = str(fib_first) + f" {fib_second}"
    for _ in range(2, n):
        fib_second, fib_next = fib_next, fib_second + fib_next
        fib_string += f" {fib_next}"

    # print(fib_string)     # 0 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
    # print(fib_string.split(" "))
    return fib_string


def fibonacci_recurs(n):
    if n in (1, 2):
        return 1
    return fibonacci_recurs(n - 1) + fibonacci_recurs(n - 2)


if __name__ == "__main__":
    # fibonacci_1()
    # fibonacci_2(20)
    print(fibonacci_recurs(10))     # 55
