class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        test = "".join(str(elem) for elem in digits)
        test1 = int(test) + 1
        answer = [int(char) for char in str(test1)]
        return answer
