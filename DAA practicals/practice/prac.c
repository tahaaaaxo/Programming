#include <stdio.h>

int fibo(int n)
{
    if (n <= 1)
        return n;
    return fibo(n - 1) + fibo(n - 2);
}

int main()
{
    int n = 10;
    printf(fibo(n));
    return 0;
}
