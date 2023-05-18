class Solution(object):
    def romanToInt(self, s):
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
        "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        total = 0
        prev_value = 0
        for i in reversed(s):
            value = romans[i]
            if value >= prev_value:
                total += value
            else:
                total -= value
            prev_value = value
        return total
                
                
            