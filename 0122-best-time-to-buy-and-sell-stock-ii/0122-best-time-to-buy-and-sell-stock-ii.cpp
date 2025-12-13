class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int min=0;
        int profit=0;
        for(int i=0;i<n-1;i++){
           if(prices[i] < prices[i+1]){
            min = prices[i];
           profit += prices[i+1] - min;
           }
           profit = max(0,profit);
        }
        
        return profit;
    }
};