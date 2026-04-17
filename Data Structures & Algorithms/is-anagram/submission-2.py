class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return true if the strings are anagrams
        #return false if they aren't
        #break down each string into an array and check if all the elemnts are the same
        #i'll probably use a hashset for this too even though this may be subpar in space complexity because I am creating an array and a hashset

        #after watching the solution guide and my solution failing I'm realizing I didn't account for multiple of the same character
        #first thing is anagrams should have the exact same length and sorted string I could compare sorted string but for the sake of practice I will use 2 hash maps

        if len(s) != len(t):
            return False
        
        mapt = {}
        maps = {}

        for i in t:
            try:
                mapt[i] += 1
            except KeyError:
                mapt[i] = 1
        
        for i in s:
            try:
                maps[i] += 1
            except KeyError:
                maps[i] = 1

        if mapt != maps:
            return False
        
        return True