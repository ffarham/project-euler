public class Solution{
    public static void main(String[] args){
        int num = 0;
        for(int i = 100; i <= 999; i++){
            for(int j = 100; j <= 999; j++){
                int product = i * j;
                if(isPalindrome(product)){
                    num = product > num ? product : num;
                }
            }
        }
        System.out.println("Ans: " + num);
    }

    private static boolean isPalindrome(int n){
        int num = n, reverseNum = 0, remainder;
        while(num != 0){
            remainder = num % 10;
            reverseNum = reverseNum * 10 + remainder;
            num /= 10;
        }
        return n == reverseNum;
    }
}