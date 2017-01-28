#include <stdio.h>

int maximum(int ar[], int n)
{

    if (n == 1) {
        return ar[0];

    } else {
        int max = maximum(ar, n-1);
        printf("Largest element : %d\n", max);
        //return 5; 
        return ar[n-1] > max ? ar[n-1] : max;
    }
}

int main()
{
    int array[5] = {5, 23, 28, 7, 1};
    printf("Maximum element of the array is: %d \n", maximum(array, 5));
    return 0;
}