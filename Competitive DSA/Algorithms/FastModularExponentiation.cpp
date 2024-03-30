#include <bits/stdc++.h>

using namespace std;

int modularExponentiation(int x, int n, int m) {
    int count = 1;

    //x^n = (x^n/2)^2 if even
    //x^n = [(x^n/2)^2 * x] if odd

    while(n > 0){

        if(n & 1){
            count = (1LL * (count % m) * (x % m)) % m;
        }

        x = (1LL * (x % m)*(x % m))%m;
        n = n >> 1;
    }

    return count % m;
}
