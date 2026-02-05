class Solution {
public:
    bool isTrionic(vector<int>& nums) {
        int a=-1;
        int b = -1;
        bool flag = false;
        for(int i=1;i<nums.size();i++){
            if (nums[i-1] < nums[i]){
                a = i;
            }
            else{
                break;
            }
        }
        if (a>0){
            for (int i=a+1;i<nums.size();i++){
                if (nums[i-1]>nums[i]){
                b = i;
            }
                else{
                    break;
                }
            }
        }
        int c=-1;
        if (b>0){
            for(int i=b+1;i<nums.size();i++){
                if(nums[i-1]<nums[i]){
                    flag =  true;
                    c = i;
                }
                else{
                    break;
                }

            }
        }
        if(c>0){
            for(int i=c+1;i<nums.size();i++){
                if (nums[i-1] >= nums[i]){
                    return false;
                }
            }
        }
        
        return flag;
    }
};