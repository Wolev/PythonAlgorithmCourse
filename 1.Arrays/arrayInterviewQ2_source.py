# Design an algorithm that checks if a string is a palindrome or not

def palindrome(string):
    if string == string[::-1]:
        print(string + " is a palindrome")
    else:
        print(string + " is NOT a palindrome")

if __name__ == "__main__":

    name1 = "rain"
    name2 = "radar"

    palindrome(name1)
    palindrome(name2)