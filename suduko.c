#include <stdio.h>

int board[9][9] = {
    {7, 8, 0, 4, 0, 0, 1, 2, 0},
    {6, 0, 0, 0, 7, 5, 0, 0, 9},
    {0, 0, 0, 6, 0, 1, 0, 7, 8},
    {0, 0, 7, 0, 4, 0, 2, 6, 0},
    {0, 0, 1, 0, 5, 0, 9, 3, 0},
    {9, 0, 4, 0, 6, 0, 0, 0, 5},
    {0, 7, 0, 3, 0, 0, 0, 1, 2},
    {1, 2, 0, 0, 0, 7, 4, 0, 0},
    {0, 4, 9, 2, 0, 6, 0, 0, 7}};

void print_board()
{
    int i, j;

    for (i = 0; i < 9; i++)
    {
        for (j = 0; j < 9; j++)
        {
            printf("%d ", board[i][j]);

            if ((j + 1) % 3 == 0 && j != 0 && j + 1 != 9)
            {
                printf("| ");
            }

            if (j == 8)
            {
                printf("\n");
            }

            if (j == 8 && (i + 1) % 3 == 0 && i + 1 != 9)
            {
                printf("- - - - - - - - - - - \n");
            }
        }
    }
}

int possible(int x, int y, int n)
{
    int i, j;

    for (i = 0; i < 9; i++)
    {
        if (board[x][i] == n)
        {
            return 0;
        }
    }

    for (j = 0; j < 9; j++)
    {
        if (board[j][y] == n)
        {
            return 0;
        }
    }

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            if (board[((x / 3) * 3) + i][((y / 3) * 3) + j] == n)
            {
                return 0;
            }
        }
    }

    return 1;
}

void solve()
{
    int i, j, n;
    for (i = 0; i < 9; i++)
    {
        for (j = 0; j < 9; j++)
        {
            if (board[i][j] != 0)
            {

                for (n = 0; n < 10; n++)
                {
                    if (possible(i, j, n) == 1)
                    {
                        board[i][j] = n;
                    }
                }
            }
        }
    }
}

int main()
{
    print_board();
    solve();
    print_board();
}