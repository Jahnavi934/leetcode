class Solution {
    public int longestSubarray(int[] nums) {
        int c = 0,h = 0,maxi = 0, c1 = 0;
        for(int i = 0; i < nums.length;i++)
        {
            if(nums[i] == 1)
            {
              c++;
              if(h==1)
              {
                c1++;
                System.out.println(i);
              }
            }
            else if(nums[i] == 0)
            {
              if(i!=0)
              {
              h++;
              }
              if(h==2)
              {
                h = 1;
                maxi = Math.max(c,maxi);
                c = c1;
                System.out.println(c);
                c1 = 0;
              }
            }
        }
        if(c == nums.length)
        {
          return c-1;
        }
        return Math.max(maxi,c);
        
    }
}