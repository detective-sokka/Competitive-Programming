class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

    #  If you are top right cell bottom left cell -- automatically included
    #  Top row - Pacific Ocean True
    #  First Column - Pacific Ocean True
    #  Last Column - Atlantic Ocean True
    #  Bottom row - Atlantic Ocean True

        result = []

        if not heights:
            return result

        pacific = set()
        atlantic = set()

        rowLen, colLen = len(heights), len(heights[0])

    def isPacific(r, c):
        return r == 0 or c == 0

    def isAtlantic(r, c):
        return r == rowLen - 1 or c == colLen - 1

    def atlanticDFS(i, j):
        stack = []
        if (i, j) not in atlantic:
            stack.append((i, j))

            while stack:
                i, j = stack.pop()

                atlantic.add((i, j))
                val = heights[i][j]

                if i + 1 < rowLen and val <= heights[i+1][j] and (i+1, j) not in atlantic:
                    stack.append((i+1, j))

                if j + 1 < colLen and val <= heights[i][j+1] and (i, j+1) not in atlantic:
                    stack.append((i, j + 1))

                if i - 1 >= 0 and val <= heights[i-1][j] and (i-1, j) not in atlantic:
                    stack.append((i-1, j))

                if j - 1 >= 0 and val <= heights[i][j-1] and (i, j-1) not in atlantic:
                    stack.append((i, j - 1))

        def pacificDFS(i, j):

            stack = []
            if (i, j) not in pacific:
                stack.append((i, j))

            while stack:
                i, j = stack.pop()

                pacific.add((i, j))
                val = heights[i][j]

                if i + 1 < rowLen and val <= heights[i+1][j] and (i+1, j) not in pacific:
                    stack.append((i+1, j))

                if j + 1 < colLen and val <= heights[i][j+1] and (i, j+1) not in pacific:
                    stack.append((i, j + 1))

                if i - 1 >= 0 and val <= heights[i-1][j] and (i-1, j) not in pacific:
                    stack.append((i-1, j))

                if j - 1 >= 0 and val <= heights[i][j-1] and (i, j-1) not in pacific:
                    stack.append((i, j - 1))

            for i, j in product(range(1), range(colLen)):
                pacificDFS(i, j)

            for i, j in product(range(rowLen), range(1)):
                pacificDFS(i, j)

            for i, j in product(range(rowLen-1, rowLen), range(colLen)):
                atlanticDFS(i, j)

            for i, j in product(range(rowLen), range(colLen-1, colLen)):
                atlanticDFS(i, j)

            return list(set.intersection(atlantic, pacific))


sol = Solution()
sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])

