#include <stdio.h>
/*

*/

int main(){
    int evenSum = 0;
    int newValue = 0;
    int x = 1, y = 1;
    while(newValue <= 4000000){
        newValue = x + y;
        if(newValue % 2 == 0){evenSum += newValue;}
        y = x;
        x = newValue;
    }
    printf("ans: %d\n", evenSum);
    return 0;
}