#include <iostream>
#include <vector>
#include <string>

int main()
{
    vector<int> v(5, vector<int>(5));
    int test_matrix[5][5] = {
        
        
    // v.push_back

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            v[i][j] = test_matrix[i][j];
        }
    }

    printf(v)
}