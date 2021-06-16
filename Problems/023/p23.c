#include <stdio.h>

int main(){
  int limit = 28123;
  //initialises array of size = limit
  int abundantNum[limit];
  int sumOfAbundant[limit];

  int i;
  //loops through all positive integers upto the limit
  for(i = 0; i < limit; i++){
    //if number is abundant
    if(isAbundant(i+1) == 1){
      //mark as an abundant number
      abundantNum[i] = 1;
    }else{
      //mark as a non-abundant number
      abundantNum[i] = 0;
    }
  }
  int j, k;
  for (j = 0; j < limit; j++){
    for(k = j; k < limit; k++){
      //if both numbers are abundant
      if(abundantNum[j] == 1 && abundantNum[k] == 1){
        //sums 2 abundant numbers together
        int sum = (j+1) + (k+1);
        //only considers numbers <= limit
        if(sum <= limit){
          //-1 represents that this number is a sum of 2 abundant numbers
          sumOfAbundant[sum-1] = -1;
        }else{
          //no need to consider numbers > than the limit as they can be written as the sum of 2 abundant numbers
          break;
        }
      }
    }
  }
  int l, total = 0;
  //loops through all numbers upto the limit
  for(l = 0; l < limit; l++){
    //if that number can not be written as a sum of 2 abundant numbers
    if(sumOfAbundant[l] != -1){
      //add it to the total
      total += l+1;
    }
  }
  //prints sum of all the positive integers which cannot be written as the sum of two abundant numbers
  printf("Answer: %d\n", total);
}

int isAbundant(int num){
  int sumofPD = 0;
  int i;
  //the biggest perfect divisor is half the number 
  for (i = 1; i <= (num+1)/2; i++){
    if (num % i == 0){
      sumofPD += i;
    }
  }
  if(sumofPD > num) return 1;
  else return 0;
}
