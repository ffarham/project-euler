public class Solution{
    public static void main(String[] args){
        int sum = 0;                            
        for(int i = 1; i < 1000; i++){         
            if(isMultiple(i)){sum += i;}        // updates the sum if i is a multiple
        }
        System.out.println("Ans: " + sum);
    }

    /* returns true if the given int is either a multiple of 3 or 5 and false otherwise */
    private static boolean isMultiple(int n){
        return n % 3 == 0 || n % 5 == 0;
    }
}