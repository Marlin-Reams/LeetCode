class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set('aeiou')
        n = len(s)
        vowel_count = [0] * (n + 1)

        for i in range(1, n + 1):
            vowel_count[i] = vowel_count[i - 1] + (s[i - 1] in vowels)

        max_vowels = 0

        for i in range(k, n + 1):
            current_vowels = vowel_count[i] - vowel_count[i - k]
            max_vowels = max(max_vowels, current_vowels)

        return max_vowels