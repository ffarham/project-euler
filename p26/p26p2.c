#include <stdio.h>
#include <math.h>

int mod(int a, int b, int n){
  //printf("11\n");
  //base case
  if(b <= 1){
    int z = pow(a,b);
    return z%n;
  }else{
    //if power is even
    if(b%2 == 0){
      //base^(b) % n = [(base^(b/2) % n)*(base^(b/2) % n)] % n
      int x = mod(a, b/2, n);
      x *= x;
      return x%n;
    }
    //if power is odd
    else{
      //base^(b) % n = [(base^(b-1) % n)*(base^(1) % n)] % n
      int y = mod(a, b-1, n) * mod(a, 1, n);
      return y%n;
    }
  }
}

int s_calc(int d){
  int count = 0;
  while(1){
    if(d%2 == 0){
      count++;
      d /= 2;
    }else if(d%5 == 0){
      count++;
      d /= 5;
    }else{
      break;
    }
  }
  return count;
}

int is_a_nonregular_decimal(int d){
  int check = 0;
  int loop = 1;
  while(loop == 1){
    if(d%2 == 0){
      if(d == 2){
        loop = 0;
      }
      d /= 2;
    }else if(d%5 == 0){
      if(d == 5){
        loop = 0;
      }
      d /= 5;
    }else{
      check = 1;
      loop = 0;
    }
  }
  return check;
}

int main(){
  int base = 10;
  int total = 0;
  int ans = 0;
  int d;
  for(d = 2; d < 1000; d++){
    //printf("\n");
    //if the fraction is nonregular
    if(is_a_nonregular_decimal(d) == 1){
      //printf("d: %d\n", d);
      //calculate s value
      int s = s_calc(d);
      //printf("s: %d\n", s);
      //calculate 10^s mod d
      int tenS_mod_d = mod(base, s, d);
      //printf("10^(s) mod d: %d\n", tenS_mod_d);
      //increment t until 10^s is congurent to 10^(s+t) mod d
      int t;
      for(t = 1; t < d; t++){
        //calculate 10^(s+t) mod d
        int tenSplusT_mod_d = mod(base, s+t, d);
        //printf("t: %d\n", t);
        //printf("10^(s+t) mod d: %d\n", tenSplusT_mod_d);
        //if they are congurent
        if(tenS_mod_d == tenSplusT_mod_d){
          //t represents the decimal period
          //printf("d: %d  t: %d  total: %d  ans: %d\n", d, t, total, ans);
          if(t > total){
            //printf("checking...\n" );
            total = t;
            ans = d;
          }
          break;
        }
      }

    }
  }
  printf("ans: %d\ntotal: %d\n", ans, total);

}
