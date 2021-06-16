#include <stdio.h>
#include <math.h>

int main(){
  int const digits = 1000;
  double const logroot5 = log10(sqrt(5));
  double const logPhi = log10( (1+sqrt(5)) / 2);

  int index = 1;
  while(index > 0){
    double numofdigits = ((index*logPhi) - logroot5) + 1;
    //printf("%lf\n", numofdigits);
    if (numofdigits >= digits){
      printf("First index to have %d digits: %d\n", digits, index);
      break;
    }else{
      index++;
    }
  }

}
