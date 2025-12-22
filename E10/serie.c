#include <stdio.h>
#include <math.h>

double fibonacci(int n) {
    // calcolo sucessione di fibonacci fino al termine n
    if (n == 1){
        return n;
    }
    else if ( n == 2) {
        return 1;
    }
    else {
        int a = 1;
        int b = 1;
        int c;
        for(int i=2; i<n; i++) {
            c = a+b;
            a = b;
            b = c;
        }
        return (double)b/a;
    }
}