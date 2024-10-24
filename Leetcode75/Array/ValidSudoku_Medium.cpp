#include <set>
#include <vector>

class Solution {
public:
    bool isValidSudoku(std::vector<std::vector<char>>& board) {
        
        int box = 0;
        int rowSize = 9, colSize = 9;
        std::set<char> rows[rowSize];
        std::set<char> cols[colSize];
        std::set<char> subBoxes[rowSize];
    
        for (int i=0; i < rowSize; i++)
        {
            for (int j=0; j < colSize; j++)
            {                   
                if (board[i][j] == '.')
                    continue;
                
                if (rows[i].find(board[i][j]) != rows[i].end())
                {
                    return false;
                }
                if (cols[j].find(board[i][j]) != cols[j].end())
                {
                    return false;
                }
                box = (i/3) * 3 + (j/3);                
                if (subBoxes[box].find(board[i][j]) != subBoxes[box].end())
                {
                    return false;
                }
                rows[i].insert(board[i][j]);
                cols[j].insert(board[i][j]);
                subBoxes[box].insert(board[i][j]);
            }
        }

        return true;
    }
};

int main()
{
    return 0;
}