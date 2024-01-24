class Solution {
    public boolean divisorGame(int n) {
        // int i=1;
        // int cnt = 0;
        // while(n>1){
        //     if(n%i ==0)
        //     {
        //         n-=i;
        //     }
        //     i+=1;
        //         cnt +=1;
        // }
        // if(cnt %2==0)
        //     return false;
        // return true;
        if(n%2==0)
            return true;
        else
            return false;
    }
}