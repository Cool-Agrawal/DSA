class Solution {
public:
    vector<int> constructTransformedArray(vector<int>& nums) {
        vector <int> res;
        int n = nums.size();
        for(int i=0;i<nums.size();i++){
            int target = (i+nums[i]%n + n)%n;
            res.push_back(nums[target]);
        }
        return res;
    }
};