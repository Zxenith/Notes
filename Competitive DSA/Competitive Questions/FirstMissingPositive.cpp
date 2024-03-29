#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

int firstMissing(int arr[], int n)
{
    sort(&arr[0],&arr[n-1]);

    int flag = 1;

    for(int i=0; i<n; i++){
        if(arr[i]<=0){
            continue;
        }
        else if(arr[i] == flag){
            flag++;
            continue;
        }
        else{
            return flag;
        }
    }

    return flag;
}

int main(){
    int popp[5] = {1,2,5,3,7};
    cout<<firstMissing(popp,5);
}
