#include <stdio.h>
int main() {
    int t;
    scanf("%d\n", &t);
    for (int i=1; i <= t; i++) {
        int x, y;
        scanf("%d %d", &x, &y);
        printf("%d\n", x + y );
    }
    return 0;
}