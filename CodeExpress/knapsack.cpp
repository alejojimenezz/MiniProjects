#include <iostream>
#include <vector>
using namespace std;

int knapsack(int capacity, vector<int> &weights, vector<int> &values, int n)
{
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));

    for (int i = 1; i <= n; i++)
    {
        for (int w = 0; w <= capacity; w++)
        {
            if (weights[i - 1] <= w)
            {
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]);
            }
            else
            {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    return dp[n][capacity];
}

int main()
{

    int n, capacity;
    n = 3;
    capacity = 50;

    vector<int> values(n), weights(n);
    cout << "Ingrese los valores de los objetos:\n";
    for (int i = 0; i < n; i++)
        cin >> values[i];
    cout << "Ingrese los pesos de los objetos:\n";
    for (int i = 0; i < n; i++)
        cin >> weights[i];

    int maxValue = knapsack(capacity, weights, values, n);

    cout << "El valor maximo que se puede obtener es: " << maxValue << endl;

    return 0;
}