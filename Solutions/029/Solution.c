//returns 1 less than the answer


#include <stdio.h>
#include <math.h>

int main(){
  int limit;
  printf("n: ");
  scanf("%d", &limit);
  printf("limit: %d\n", limit);
  int total = pow(limit-1, 2);
  int i, j;
  for(i = 2; i <= limit; i++){
    //printf("checking i: %d\n", i);
    for(j = 2; j <= limit; j++){
        //if(check(i, j, limit)){
          //total--;;
        //}
        //printf("total: %d\n", total);
        total -= check(i, j, limit);
    }
  }
  printf("ans: %d\n", total);
}

int check(int n, int m, int limit){
  int a, b, baseofn, powerofn;
  for(a = 2; a < n; a++){
    for(b = 2; b <= n; b++){
      if(pow(a, b) == n){
        baseofn = a;
        powerofn = b*m;
      }
    }
  }
  //int dups = 0;
  int i, j;
  for(i = 2; i < n; i++){
    for(j = 2; j <= n; j++){
      int baseofi, powerofi;
      //base form of i,j
      if(i > 3){

        int k, l;
        for(k = 2; k < i; k++){
          for(l = 2; l <= i; l++){
            if(pow(k, l) == i){
              baseofi = k;
              powerofi = l*j;
            }
          }
        }
      }else{
        baseofi = i;
        powerofi = j;
        printf("baseofi: %d  powerofi: %d", baseofi, powerofi);
      }

      if(baseofi == baseofn && powerofi == powerofn){
        printf("n: %d  m: %d\n", n, m);
        printf("baseofn: %d  powerofn: %d\n", baseofn, powerofn);
        printf("baseofi: %d  powerofi: %d\n", baseofi, powerofi);
        //printf("j*m: %d\n", j*m);
        //dups++;
        //printf("i: %d  j*m: %d  n: %d  m: %d  j: %d\n", i, j*m, n, m, j);
        return 1;
      }

    }
  }
  //return dups;
  return 0;
}
