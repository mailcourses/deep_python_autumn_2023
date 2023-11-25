#include <stdlib.h>
#include <stdio.h>

struct Point
{
    int x;
    int y;
};

int area(struct Point* p1, struct Point* p2)
{
    return abs((p1->x - p2->x) * (p1->y - p2->y));
}

int sum(int* arr, int len)
{
    int res = 0;
    for (int i = 0; i < len; i += 1)
    {
        res += arr[i];
    }
    return res;
}

int fibonacci(int n)
{
    if (n < 2)
    {
        return 1;
    }
    return fibonacci(n-2) + fibonacci(n-1);
}
