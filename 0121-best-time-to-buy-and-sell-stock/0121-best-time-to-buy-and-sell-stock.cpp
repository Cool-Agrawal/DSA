class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int min = prices[0];
        int min_pos = 0;
        int max_profit = 0;
        for(int i=1;i<n;i++){
            if(prices[i] < min){
                min = prices[i];
                min_pos =i;
            }
        
         else {
                max_profit = max(max_profit, prices[i] - min);
            }
        }
        return max_profit;
    }
};