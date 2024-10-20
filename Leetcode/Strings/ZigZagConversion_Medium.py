# Note: The if conditions can be simplified

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        rows = [''] * numRows
        index = 0
        increment = True
        for c in s:
            rows[index] = rows[index] + c

            if index == numRows - 1:
                increment = False
                index = index - 1
            elif index == 0:
                increment = True
                index = index + 1
            else:
                if increment:
                    index = index + 1
                else:
                    index = index - 1
        return ''.join(rows)