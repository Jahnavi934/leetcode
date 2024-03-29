class Solution {
    public int getMaximumGenerated(int n) {
        if(n==0)
            return 0;
        int[] dp = new int[n+1];
        dp[0] = 0;
        dp[1] = 1;
        for(int i=2;i<=n;i++)
        {
            if(i%2==0)
                dp[i] = dp[i/2];
            else{
                int a = (int)(i/2);
                dp[i] = dp[a] + dp[a+1];
            }
        }
        int maxi = 0;
        for(int i=0;i<dp.length;i++){
            System.out.print(dp[i]);
            if(dp[i] > maxi)
                maxi = dp[i];
        }
        return maxi;
    }
}