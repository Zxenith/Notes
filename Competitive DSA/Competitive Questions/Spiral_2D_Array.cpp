#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> order;

        int r = matrix.size();
        int c = matrix[0].size();

        int sr = 0;
        int sc = 0;
        int er = r - 1;
        int ec = c - 1;

        int count = 0;
        int total = r * c;

        while(count < total){
            for(int i = sc; count < total && i <= ec; i++){
                order.push_back(matrix[sr][i]);
                count++;
            }
            sr++;

            for(int i = sr; count < total && i <= er; i++){
                order.push_back(matrix[i][ec]);
                count++;
            }
            ec--;

            for(int i = ec; count < total && i >= sc; i--){
                order.push_back(matrix[er][i]);
                count++;
            }
            er--;

            for(int i = er; count < total && i >= sr; i--){
                order.push_back(matrix[i][sc]);
                count++;
            }
            sc++;
        }
        return order;
    }
};
