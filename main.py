# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


# def find_anagram(word, anagram):
#     # [assignment] Add your code here
#     word = input("word:")
#     anagram = input("anagram:")
#     sorted_word = sorted(word)
#     sorted_anagram = sorted(anagram)
    
    
#     if sorted_word == sorted_anagram:
#         print ("True")
        
#     else:
#         print ("False")
class Solution:
    def find_anagram(self, word: str, anagram: str) -> list[int]:
        if len(word) > len(anagram): return []
        anagramCount, wordCount = {}, {}
        for i in range(len(anagram)):
            anagramCount[anagram[i]] = 1 + anagramCount.get(anagram[i], 0)
            wordCount[word[i]] = 1 + wordCount.get(word[i], 0)
            
        result = [0] if wordCount == anagramCount else []
        l = 0
        for r in range(len(anagram), len(word)):
            wordCount[word[r]] = 1 + wordCount.get(word[r], 0)
            wordCount[word[l]] -= 1
            
            if wordCount[word[l]] == 0:
                wordCount.pop(word[l])
            l += 1
            if wordCount == anagramCount:
                result.append(l)
        return result
