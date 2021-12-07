# Interview Question #4
# Construct an algorithm to check whether two words (or phrases) are anagrams or not!
# For example: restful and fluster

def anagram(word1,word2):
    return sorted(word1) == sorted(word2)

if __name__ == "__main__":
    print(anagram("restful", "fluster"))