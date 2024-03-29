class Solution {
public:
    int countPrimes(int n) {
        int count = 0;
        vector<bool> mark(n+1,true);

        mark[0] = mark[1] = false;

        for(int i = 2; i < n; i++){
            if(mark[i]){
                count++;

                for(int j = 2*i; j < n; j += i){
                    mark[j] = false;
                }
            }
        }
        return count;
    }
};
