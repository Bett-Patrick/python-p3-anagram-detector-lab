# your code goes here!

class Anagram:
    def __init__(self,search_word):
        self.search_word = search_word
    def match(self,possible_anagrams):
        anagrams = []
        for word in possible_anagrams:
            if sorted(self.search_word.lower()) == sorted(word) and possible_anagrams != 0:
                anagrams.append(word)
        return anagrams


            
        
