class Solution {
public:
    bool isBalanced(string num) {
        int n = num.size();
        int a = 0;
        int b = 0;
        for(int i=0;i<n;i+=2){
            a += num[i]-'0';
        }
        cout<<a;
        for(int i=1;i<n;i+=2){
            b += num[i]-'0';
        }
        cout<<b;
        return a==b;
    }
};