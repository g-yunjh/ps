#include <stdio.h>
int main() {
    int n, x;
    scanf("%d %d", &n, &x);
    int arr;
    for (int i = 0; i < n;i++) {
        scanf("%d", &arr);
        if (arr < x) {
            printf("%d ", arr);
        }
    }

    return 0;
}