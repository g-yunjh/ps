#include <stdio.h>
int main() {
    int n;
    int x = 0;
    scanf("%d", &n);
    for (int i = 0; i <= n;i++) {
        x = x + i;
    }
    printf("%d", x);
    return 0;
}