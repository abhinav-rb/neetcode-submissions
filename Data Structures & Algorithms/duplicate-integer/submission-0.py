class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #3 options - 1 go through every number in the set and compare to every other number in the set O(n^2)
        # Option 2 - Sort list least to greatest then go through and compare each number to the next O(nlogn)
        # Option 3 - Add each number to a hash and if the number is already in the hash then return true

        hashset = set()

        for n in nums:
            if n in hashset:
                return True;
            hashset.add(n)
            
        return False;
        