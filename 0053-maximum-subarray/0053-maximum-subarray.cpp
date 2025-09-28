class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int max_sum =nums[0],current= nums[0];
        for(int i=1;i<n;i++){
            current = max(nums[i], current + nums[i]);
            max_sum = max(current,max_sum);
        }
        return max_sum;
    }
};