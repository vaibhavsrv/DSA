class Solution {
public:
    int findMin(vector<int>& nums) {
        int ans = INT_MAX;
        for(auto &it : nums)
        {
            ans = min(ans, it);
        }
        return ans;
    }
};