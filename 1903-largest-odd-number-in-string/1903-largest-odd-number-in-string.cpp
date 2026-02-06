class Solution {
public:
    string largestOddNumber(string num) {
        int n = num.size()-1;
        int a = -1;
        for(int i=n;i>=0;i--){
            if ((num[i] - '0')%2 != 0){
                 a = i;
                break;

            }
        }
        string s = "";
        for(int i=0;i<=a;i++){
            s += num[i];
        }
        return s;
    }
};