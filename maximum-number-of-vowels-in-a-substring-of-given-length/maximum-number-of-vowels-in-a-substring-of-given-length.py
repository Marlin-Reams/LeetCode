class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set('aeiou')
        window = s[:k]
        vowel_count = sum(1 for c in window if c in vowels)
        max_vowels = vowel_count
        
        for i in range(k, len(s)):
            vowel_count += (s[i] in vowels) - (s[i-k] in vowels)
            max_vowels = max(max_vowels, vowel_count)
            if max_vowels == k:
                return max_vowels
        
        return max_vowels