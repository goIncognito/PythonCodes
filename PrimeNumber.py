def num_is_prime(num):
    flag = True
    if num < 2:
        print("Please enter a positive integer greater than 1")

    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                flag = False
                break

        if flag:
            print("The number is Prime Number")
        else:
            print("The number is not Prime Number")

number = int(input("Enter a number to check Prime: "))
num_is_prime(number)
