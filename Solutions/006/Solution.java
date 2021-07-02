public class Solution{
    public static void main(String[] args){
        int sum = 0;
        int sumofsquares = 0;
        for(int i = 1; i <= 100; i++){
            sum += i;
            sumofsquares += i*i;
        }
        int squareofsum = sum * sum;
        System.out.println("Ans: " + (squareofsum - sumofsquares));
    }
}