#include <stdio.h>
#include <math.h>
#include <limits.h>
int main(void)
{
    int n;
    scanf("%i", &n);
    int arr[n];
    for(int i = 0; i < n; i++){
        scanf("%i", &arr[i]);
    }

    for(int i = 0; i < n - 1; i += 2){
        // swap arr[i] with arr[i+1]
        int temp = arr[i];
        arr[i] = arr[i+1];
        arr[i + 1] = temp;
    }

    for(int i = 0; i < n; i++){
        printf("%i ", arr[i]);
    }

}
