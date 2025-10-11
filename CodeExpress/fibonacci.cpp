#include <iostream>
#include <vector>
using namespace std;

vector<long long> memo;

long long fibonacci(int n)
{
    if (n <= 1)
        return n;
    if (memo[n] != -1)
        return memo[n];
    return memo[n] = fibonacci(n - 1) + fibonacci(n - 2);
}

int main()
{
    int n;
    cout << "Ingrese un numero: ";
    cin >> n;

    memo.assign(n + 1, -1);

    cout << "Fibonacci(" << n << ") = " << fibonacci(n) << endl;
    return 0;
}