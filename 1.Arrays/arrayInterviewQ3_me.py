# Our task is to design an efficient algorithm to reverse a given integer.

def reverse(number):

    reversed_num = 0
    remainder = 0

    while (number > 0):
        remainder = number % 10
        number = number // 10
        reversed_num = reversed_num * 10 + remainder

    return reversed_num

if __name__ == "__main__":
    print(reverse(1234))
    print(reverse(123456789))


