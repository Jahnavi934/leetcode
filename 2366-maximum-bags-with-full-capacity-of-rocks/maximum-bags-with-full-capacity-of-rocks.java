class Solution {
    public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        int sum = 0,sum1 = 0,v = 0;
        int arr[] = new int[capacity.length];
        for(int i = 0 ; i< capacity.length;i++)
        {
           arr[i] = capacity[i]-rocks[i];
           v += 1;
        }
        Arrays.sort(arr);
        int k = 0,c = 0;
        for(int j = 0 ; j < v ; j++)
        {    
             if(arr[j] == 0)
             {
                 c += 1;
             }
             else
             {
                if(additionalRocks >= arr[j]) 
                {
                    additionalRocks -=arr[j];
                    c +=1;
                 }
                else
                {
                 break;
                }
             }
        }
        return c;
       
    }  
    
}