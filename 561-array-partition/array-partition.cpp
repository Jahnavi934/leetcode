class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        int n = size(nums);
        sort(begin(nums), end(nums));

        int ans=0;
        for(int i=0; i<n; i+=2)
        {
            ans+=nums[i];
        }
        return ans;
    }
};