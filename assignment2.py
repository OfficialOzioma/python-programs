def num_of_cases():
    print("FIRST LETS CHECK \nTHE NUMBER OF UPPER AND LOWER CASE \nCHARACTERS IN ANY WORD(S)")
    print("\n")
    words = input("Please any word or words ")

    UPPER_CASE = 0
    lower_case = 0

    for case in words:
        if case.isupper():
            UPPER_CASE += 1
        elif case.islower:
            lower_case += 1
        else:
            pass
    print ("Your entered the following words", words)
    print ("Number of Upper case characters are ", UPPER_CASE)
    print ("Number of Lower case Characters are ", lower_case)
    print("\n")

num_of_cases()

def prime():
    print("Now LETS CHECK \nIF A NUMBER IS PRIME OR NOT")
    print("\n")
    num = input("Enter the prime number \n")
    number = int(num)
    if type(number) is not int:
        return print("{} is not prime Number".format(number))
    if number < 1 or number == 1:
        return print("{} is not prime Number".format(number))
    for i in range(2, number):
        if number % i == 0:
            return print("{} is not prime Number".format(number))

    print("{} is prime Number".format(number))
    print("\n")

prime()

def maximum():
    print("NOW LETS CHECK \nTHE MAXIMUM OF ANY THREE NUMBERS")
    print("\n")
    num1 = input("Please the First Number ")
    num2 = input("Please the second Number ")
    num3 = input("Please the third Number ")
    if num1 > num2 and num1 > num3:
        print('The first number is the maximum', num1)
    elif num2 > num1 and num2 > num3:
        print('The second number is the maximum', num2)
    elif num3 > num1 and num3 > num2:
        print('The third number is the maximum', num3)

maximum()