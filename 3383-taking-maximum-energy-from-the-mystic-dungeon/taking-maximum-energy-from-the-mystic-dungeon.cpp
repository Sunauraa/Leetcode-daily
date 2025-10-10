class Solution {
public:
    int maximumEnergy(vector<int>& energy, int k) {
        int n = energy.size();
        vector<int> dp(n);
        int ans = INT_MIN;
        for ( int i = 0 ; i < n ; i++)
        {
            if (i>=k)
            {
                dp[i] = max(0,dp[i-k]) + energy[i];
            }
            else{
                dp[i] = energy[i];
            }
            if (i >= n-k) ans = max(ans,dp[i]);
        }
        return ans;
    }
};