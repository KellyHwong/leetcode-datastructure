#include <iostream>

using namespace std;

int cnts[101];

int main()
{
    int sugar, k;
    for (int i = 0; i < 10; i++)
    {
        cin >> sugar;
        cnts[sugar]++;
    }
    cin >> k;
    int ans = 0;
    for (int i = 100; i >= 1; i--)
    {
        if (cnts[i] != 0)
            k--;
        if (k == 0)
        {
            ans = i;
            break;
        }
    }
    cout << ans << endl;
    return 0;
}