list_of_divisors = []

def proper_divisors(number):
    for divisor in range(1, number):
        if number % divisor == 0:
            list_of_divisors.append(divisor)

def main() -> None:
    number = int(input("Type in a number: "))
    proper_divisors(number)
    print(list_of_divisors)

if __name__ == "__main__":
    main()