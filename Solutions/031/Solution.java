public class Solution{

    public static int solution(int[] coins, int t){
        int[] values = new int[t+1];
        values[0] = 1;
        //values[t] = 1;
        for(int i = 1; i <= t; i++){
            values[i] = 0;
            for(int c : coins){
                if(i-c >= 0) values[i] += values[i-c];
            }
        }
        return values[t];
    }

    public static void main(String[] args){
        int[] coins = {1,2,5,10,20,50,100,200};
        int target = 2;
        int ans = solution(coins, target);
        System.out.println("Ans: " + ans);
    }
}