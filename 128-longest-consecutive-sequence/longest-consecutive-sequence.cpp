class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        sort( nums.begin() , nums.end());
        long long cur = 1;
        long long ans = 0;
        if( nums.size() > 0 ) ans++;
        for( long long i = 1 ; i < nums.size() ; i++ )
        {
            if( nums[i] == nums[i-1] )
                continue;
            if( nums[i] == nums[i-1]+1 )
            {
                cur++;
                ans = max(ans,cur);
            }
            else
                cur = 1;
        }
        return ans;
    }
};