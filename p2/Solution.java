public class Solution{
    public static void main(String[] args){
        int evenSum = 0;
        int newValue = 0;
        int x = 1, y = 1;
        while(newValue <= 4000000){
            newValue = x + y;
            if(newValue % 2 == 0){evenSum += newValue;}
            y = x;
            x = newValue;
        }
        System.out.println("Ans: " + evenSum);
    }
}