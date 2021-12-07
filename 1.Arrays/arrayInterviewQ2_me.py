# Design an algorithm that checks if a string is a palindrome or not

def palindrome(string):
    start_index = 0
    end_index = len(string) - 1
    string_index = 0

    while start_index < end_index:
        if string[start_index] == string[end_index]:
            string_index += 1
            start_index += 1
            end_index -= 1
        else:
            print(string + " is no palindrome")
            break

    if string_index == int(len(string) / 2):
        print(string + " is a palindrome")


if __name__ == '__main__':
    name1 = 'radar'
    name2 = 'read'
    name3 = 'madam'

    palindrome(name1)
    palindrome(name2)
    palindrome(name3)
