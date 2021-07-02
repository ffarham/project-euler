public class Solution{
    public static void main(String[] args){
        long num = 600851475143L;
        int greatestPF = 1;

        while(true){
            int x = 1;
            while(true){
                x += 1;
                if(num % x == 0){
                    long factor = num / x;
                    if(greatestPF < x){greatestPF = x;}
                    num = factor;
                    break;
                }
            }
            if(num == 1){break;}
        }
        System.out.println("Ans: " + greatestPF);
    }
}