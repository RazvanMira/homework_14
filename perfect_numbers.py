list_of_divisors = []

def proper_divisors(number):
    for divisor in range(1, number):
        if number % divisor == 0:
            list_of_divisors.append(divisor)

def perfect_number(number):
    proper_divisors(number)
    if sum(list_of_divisors) == number:
        print("The number is a perfect number.")
    else:
        print("The number is not a perfect number.")

def main() -> None:
    number = int(input("Type in a number: "))
    perfect_number(number)

if __name__ == "__main__":
    main()