#include <stdio.h>
#include <math.h>

int main(){
  int n = 1001;
  int maxNum = n*n;
  int total = 0;
  int gap = 1;
  int topRight = 9;
  int i;
  for(i = 1; i <= maxNum; i += gap+1){
    if(i == topRight){
      gap += 2;
      topRight = pow(gap+2, 2);
    }
    printf("i: %d\n", i);
    total += i;
    printf("total: %d\n", total);
  }
  printf("total: %ld\n", total);
}
