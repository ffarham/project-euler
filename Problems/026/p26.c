#include <stdio.h>
#include <math.h>
#include <stdbool.h>

int mod(long long a,int n){
  return a % n;
}

int modulo_order(int d){
  int e = 1;
  while(1){
    //printf("%d\n", e);
    long long x = pow(10, e);
    if(mod(x, d) == mod(1, d)){
      return e;
    }else{
      e++;
    }
  }
}

bool relative_prime_to_10(int d){
  return (mod(d,2) != 0 && mod(d,5) != 0);
}

int main(){
  //long y = modulo_order(999);
  //printf("%ld\n", y);


  int length = 998;
  long answer = 0;
  //int numbers[length];
  int i;
  for(i = 1; i <= length; i++){
    //printf("%d\n", i+1);
    printf("%d is relative prime to 10: %d\n", i+1,relative_prime_to_10(i+1));
    if(relative_prime_to_10(i+1)){
      long decimal_period = modulo_order(i+1);
      printf("decimal period: %ld\n", decimal_period);
      if(decimal_period > answer){
        answer = decimal_period;
      }
    }
  }

  printf("Answer: %ld\n", answer);


}
