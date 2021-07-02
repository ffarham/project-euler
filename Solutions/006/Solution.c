#include <stdio.h>

int main(){
    int sumofsquares = 0, sum = 0, i;
    for(i = 1; i <= 100; i++){
        sum += i;
        sumofsquares += i*i;
    }
    int squareofsum = sum * sum;
    printf("Ans: %d\n", squareofsum - sumofsquares);
}